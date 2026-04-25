# Envira-North AI Assistant Platform — Build Plan v2

**Author:** Claude Opus 4.6
**Date:** 2026-04-24

---

## What We're Building

A multi-tenant AI assistant platform where company employees chat with an agent grounded in their internal wiki. The agent autonomously reads wiki files per query (via the Agent SDK), so token costs stay low. Each client (Envira-North, Full Gauge Controls, etc.) gets their own branded instance with separate wiki, theme, and conversation history.

**Key capabilities:**
- Professional chat UI with custom branding (logo, colors, fonts)
- Image and video rendering in chat messages
- Read-only Q&A mode (default) + admin edit mode for wiki management
- Persistent conversation history with sidebar replay
- Per-user authentication and feedback collection
- Conversation log export to S3

---

## Architecture

```
User's Browser                         Railway
┌─────────────────────┐               ┌──────────────────────────────────┐
│                     │  WebSocket    │  Chainlit (frontend + backend)   │
│  Chainlit UI        │◄────────────►│                                  │
│                     │               │  • Chat UI (bubbles, streaming)  │
│  • Logo, theme      │               │  • Auth (username/password)      │
│  • Chat history     │               │  • Session persistence           │
│  • Starter prompts  │               │  • Feedback (thumbs up/down)     │
│  • Image/video      │               │                                  │
│  • Markdown tables  │               │  Agent SDK (per query)           │
│                     │               │  ├─ Read mode: Sonnet 4.6        │
│                     │               │  │  Tools: Read, Glob, Grep      │
│                     │               │  └─ Edit mode: Opus 4.6          │
│                     │               │     Tools: + Write, Edit         │
│                     │               │                                  │
│                     │               │  wiki/ (on disk, never exposed)  │
│                     │               │  CLAUDE.md (agent instructions)  │
└─────────────────────┘               └──────────────┬───────────────────┘
                                                     │
                                      ┌──────────────┼──────────────┐
                                      │              │              │
                                      ▼              ▼              ▼
                                 Railway        Claude API      AWS S3
                                 Postgres       (Anthropic)     (log archive)
                                 (history)      (per query)     (daily cron)
```

**Why Chainlit instead of separate frontend + backend?**
- Chainlit is a full-stack Python framework (FastAPI + React under the hood)
- Chat UI, streaming, auth, session persistence, feedback — all built-in
- No need for a separate FastAPI service — Agent SDK runs inside Chainlit's message handlers
- One process to deploy, one service on Railway

---

## Project Structure

```
climtek/
├── app.py                     # Chainlit app — main entry point
├── agent.py                   # Agent SDK session management
├── config.py                  # Client config loader
├── export_logs.py             # S3 cron job script
│
├── clients/
│   └── enviranorth/
│       ├── config.toml        # Client-specific settings (name, model, limits)
│       ├── theme.json         # Colors, fonts, CSS variables
│       ├── logo_light.png     # Logo for light mode
│       ├── logo_dark.png      # Logo for dark mode
│       ├── starters.json      # Starter prompt buttons
│       └── system_prompt.md   # Client-specific system prompt additions
│
├── wiki/                      # Envira-North wiki (already exists, 65+ docs)
│   ├── CLAUDE.md              # Agent instructions — loaded into every session
│   ├── index.md
│   ├── products/
│   ├── controls/
│   ├── guides/
│   ├── comparisons/
│   ├── applications/
│   ├── image-descriptions/
│   └── glossary.md
│
├── public/                    # Chainlit static assets (copied from clients/{name}/)
│   ├── logo_light.png
│   ├── logo_dark.png
│   └── theme.json
│
├── .chainlit/
│   └── config.toml            # Chainlit configuration
│
├── requirements.txt
├── nixpacks.toml              # Railway build config
├── .gitignore
└── .env.example
```

**Multi-tenant pattern:** Each client gets their own repo clone with their own `clients/{name}/` folder and `wiki/` folder. At ~10 clients, consolidate into a single app with URL-based routing.

---

## Phase 1 — Working Product

### Core App: `app.py`

Chainlit message handlers:

```python
import chainlit as cl
from agent import create_agent_session, query_agent

# --- Auth ---
@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Check against stored credentials (env vars or DB)
    if verify_user(username, password):
        return cl.User(identifier=username, metadata={"role": get_role(username)})
    return None

# --- Welcome + Starters ---
@cl.on_chat_start
async def on_start():
    user = cl.user_session.get("user")
    await cl.Message(
        content=f"Welcome to the Envira-North Product Assistant! Ask me anything about our HVLS fans, controls, or installation guides."
    ).send()

@cl.set_starters
async def starters():
    return [
        cl.Starter(label="Compare SmartAIR vs TouchAIR", message="...", icon="/public/compare.svg"),
        cl.Starter(label="Best fan for a warehouse", message="...", icon="/public/warehouse.svg"),
        cl.Starter(label="Installation guide", message="...", icon="/public/install.svg"),
    ]

# --- Main message handler ---
@cl.on_message
async def on_message(message: cl.Message):
    user = cl.user_session.get("user")
    edit_mode = cl.user_session.get("edit_mode", False)

    # Build conversation history (rolling window — last 10 turns)
    history = cl.chat_context.to_openai()[-20:]  # 10 user + 10 assistant

    # Stream response from agent
    response_msg = cl.Message(content="")
    await response_msg.send()

    async for token in query_agent(
        message=message.content,
        history=history,
        edit_mode=edit_mode,
        wiki_path="./wiki",
    ):
        await response_msg.stream_token(token)

    await response_msg.update()

# --- Resume past conversations ---
@cl.on_chat_resume
async def on_resume(thread):
    pass  # Chainlit auto-restores messages
```

### Agent SDK: `agent.py`

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, TextBlock

READ_TOOLS = ["Read", "Glob", "Grep"]
WRITE_TOOLS = ["Read", "Glob", "Grep", "Write", "Edit"]

async def query_agent(message: str, history: list, edit_mode: bool, wiki_path: str):
    tools = WRITE_TOOLS if edit_mode else READ_TOOLS
    model = "claude-opus-4-6" if edit_mode else "claude-sonnet-4-6"

    # Load CLAUDE.md as part of the system prompt
    claude_md = open(f"{wiki_path}/CLAUDE.md").read()
    system_prompt = f"{claude_md}\n\n## Additional Instructions\n{load_client_system_prompt()}"

    options = ClaudeAgentOptions(
        allowed_tools=tools,
        system_prompt=system_prompt,
        cwd=wiki_path,
        model=model,
        thinking=ThinkingConfigAdaptive(),
        max_turns=15,
        max_budget_usd=0.50,
        include_partial_messages=True,
        permission_mode="bypassPermissions",
    )

    # Build prompt with conversation history
    prompt = build_prompt(message, history)

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        yield block.text
```

### Key behaviors:

1. **Every query:** Agent loads CLAUDE.md as system prompt → reads index.md → finds relevant files → synthesizes answer
2. **Read mode (default):** Sonnet 4.6, read-only tools. Fast, cheap, safe.
3. **Edit mode (admin toggle):** Opus 4.6, read + write tools. For wiki edits and audits.
4. **History:** Rolling window of last 10 turns sent with each query. Full history in Postgres.
5. **Wiki files stay server-side.** Never sent to the browser. Agent answers reference product names, not filenames.

---

### Authentication

Chainlit's built-in password auth:

```toml
# .chainlit/config.toml
[auth]
require_login = true
```

User accounts stored in environment variables (Phase 1) or Postgres (Phase 2):

```
USERS=admin:strongpassword123,sarah:her_password,mike:his_password
ADMINS=admin
```

Only users in `ADMINS` can toggle edit mode.

---

### Feedback

Enabled by default in Chainlit when data persistence is active. Users see thumbs up/down on every assistant message. Feedback stored in Postgres alongside the conversation.

---

### Error Handling

```python
@cl.on_message
async def on_message(message: cl.Message):
    try:
        # ... agent query ...
    except AnthropicAPIError:
        await cl.Message(
            content="Our AI assistant is temporarily unavailable. Please try again in a few minutes."
        ).send()
    except BudgetExceededError:
        await cl.Message(
            content="This question required too many lookups. Please try a more specific question."
        ).send()
    except Exception as e:
        await cl.Message(
            content="Something went wrong. Please try again or contact support."
        ).send()
        log_error(e)
```

---

### Response Formatting

The system prompt instructs the agent to:

```markdown
## Response format rules
- Use markdown tables for spec comparisons
- Use bullet points for feature lists
- End every answer with a "Sources" section listing product/control names used (NOT filenames)
- Never mention wiki filenames, file paths, or source_docs
- Keep answers concise — aim for 100-300 words unless a comparison table requires more
- If you cannot answer from the wiki, say: "I don't have that in my documentation — please contact Customer Support at 519-527-2198 or bigair@enviranorth.com."
```

---

### Branding (Envira-North)

**`public/theme.json`:**

```json
{
    "custom_fonts": [],
    "variables": {
        "light": {
            "--font-sans": "'Inter', sans-serif",
            "--primary": "142 70% 28%",
            "--primary-foreground": "0 0% 100%",
            "--background": "0 0% 100%",
            "--foreground": "0 0% 5%",
            "--radius": "0.75rem"
        },
        "dark": {
            "--font-sans": "'Inter', sans-serif",
            "--primary": "142 70% 40%",
            "--primary-foreground": "0 0% 100%",
            "--background": "0 0% 13%",
            "--foreground": "0 0% 93%"
        }
    }
}
```

**`.chainlit/config.toml`:**

```toml
[project]
name = "Envira-North Product Assistant"

[UI]
name = "Envira-North Product Assistant"
default_theme = "light"

[auth]
require_login = true
```

**Logo:** Drop `logo_light.png` and `logo_dark.png` into `public/`.

---

### Data Persistence (Postgres)

Chainlit's official data layer with Railway's built-in Postgres:

```
DATABASE_URL=postgresql://user:pass@host:5432/chainlit
```

Stores:
- Conversation threads (full message history)
- User sessions
- Feedback (thumbs up/down)
- Element metadata (images, files)

---

### S3 Log Export: `export_logs.py`

Daily cron job that exports new conversations to S3:

```python
import boto3
import json
import psycopg2
from datetime import datetime, timedelta

def export_conversations():
    # Connect to Postgres
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cursor = conn.cursor()

    # Get conversations from the last 24 hours
    yesterday = datetime.utcnow() - timedelta(days=1)
    cursor.execute(
        "SELECT id, data FROM threads WHERE created_at >= %s",
        (yesterday,)
    )

    # Upload to S3
    s3 = boto3.client("s3")
    for thread_id, data in cursor.fetchall():
        s3.put_object(
            Bucket=os.environ["S3_BUCKET"],
            Key=f"conversations/{datetime.utcnow().strftime('%Y/%m/%d')}/{thread_id}.json",
            Body=json.dumps(data),
        )

if __name__ == "__main__":
    export_conversations()
```

Railway cron service runs this daily at midnight UTC.

---

## Deployment: Railway

### Services (per client)

| Service | Type | Start Command |
|---|---|---|
| App | Web Service | `chainlit run app.py --host 0.0.0.0 --port $PORT` |
| Postgres | Database | (Railway managed — click to add) |
| S3 Export | Cron Job | `python export_logs.py` (daily at 00:00 UTC) |

### `nixpacks.toml`

```toml
[phases.setup]
nixPkgs = ["nodejs_20", "npm"]

[phases.install]
cmds = [
    "pip install -r requirements.txt",
    "npm install -g @anthropic-ai/claude-code"
]

[start]
cmd = "chainlit run app.py --host 0.0.0.0 --port ${PORT:-8000}"
```

### Environment Variables

```
ANTHROPIC_API_KEY=sk-ant-...
DATABASE_URL=postgresql://...       # Auto-set by Railway Postgres
S3_BUCKET=climtek-conversation-logs
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
USERS=admin:pass,sarah:pass
ADMINS=admin
CLIENT_NAME=enviranorth
```

### `.gitignore`

```
.env
__pycache__/
*.pyc
.chainlit/translations/
public/logo_*.png
```

---

## Local Development

```bash
# Terminal 1
cd climtek
pip install -r requirements.txt
npm install -g @anthropic-ai/claude-code   # if not already installed
export ANTHROPIC_API_KEY=sk-ant-...
export DATABASE_URL=sqlite:///local.db      # SQLite for local dev
chainlit run app.py --watch
```

Open `http://localhost:8000` in browser.

### Test queries:
- "What is the blade diameter of the 24ft geared Sailfin?" (simple spec lookup)
- "Compare SmartAIR vs TouchAIR" (comparison)
- "Best fan for a dairy barn with 25ft ceilings?" (application recommendation)
- "Which fan should I get?" (should ask clarifying questions)
- "What's the price of the 16ft gearless?" (should defer to Customer Support)

### Test edit mode (admin only):
- "Update the Sailfin 24ft page to add a note about the new mounting bracket"
- "Run a wiki audit"

---

## Cost Estimate

### Per client — monthly

| Component | Light (5 q/day) | Medium (20 q/day) | Heavy (50 q/day) |
|---|---|---|---|
| Railway compute | $5-10 | $5-10 | $10-12 |
| Railway Postgres | Free | Free | Free |
| Claude API (Sonnet read) | $6 | $24 | $60 |
| Claude API (Opus write) | ~$0 | ~$5 | ~$15 |
| AWS S3 | $1 | $1 | $2 |
| **Total** | **~$12-17** | **~$35-40** | **~$87** |

### Scaled

| Clients | Medium usage each | Monthly total |
|---|---|---|
| 1 | $39 | $39 |
| 3 | $39 | $117 |
| 5 | $39 | $195 |
| 10 | $39 | $390 |

### Cost guardrails
- `max_budget_usd=0.50` per query — hard cap
- `max_turns=15` — agent can't loop forever
- Per-user daily limit — Phase 2

---

## Build Order

| Step | What | Files |
|---|---|---|
| 1 | Scaffold | `requirements.txt`, `.gitignore`, `.env.example`, `.chainlit/config.toml`, `public/theme.json` |
| 2 | Agent module | `agent.py` — Agent SDK integration, mode switching, CLAUDE.md loading |
| 3 | Chainlit app | `app.py` — message handler, auth, starters, streaming, error handling |
| 4 | Branding | Logo files, theme.json, config.toml for Envira-North |
| 5 | System prompt | Update wiki system prompt with response format rules |
| 6 | Local test | Run locally, test Q&A + edit mode + history + feedback |
| 7 | Data persistence | Connect Chainlit to Postgres, verify sidebar history works |
| 8 | S3 export | `export_logs.py` + Railway cron setup |
| 9 | Deploy | Railway project setup, push to GitHub, share URL |

---

## Phase 2 — Enhancements (after Phase 1 works)

| Feature | Description |
|---|---|
| File upload | Users upload images/PDFs in chat — Claude vision processes them |
| Inline images | Agent renders product diagrams in answers |
| OAuth (Google/Microsoft) | Replace password auth with SSO |
| Per-user rate limits | Daily query caps, stored in Postgres |
| Monthly usage dashboard | Query counts, costs, popular topics, feedback stats |
| Model routing | Haiku for simple lookups, Sonnet for reasoning |
| Multi-tenant consolidation | Single app with URL-based client routing (at ~10 clients) |
| AskUserQuestion with buttons | Structured clarification UI instead of text-based |

---

## Locked Architecture Decisions

| # | Decision | Choice |
|---|---|---|
| 1 | Frontend | Chainlit |
| 2 | Hosting | Railway |
| 3 | Tool access | Mode-switching (read-only default, write for admins) |
| 4 | Data layer | PostgreSQL (Railway built-in) |
| 5 | Model | Sonnet 4.6 (read) + Opus 4.6 (write) |
| 6 | Compaction | Rolling window (last 10 turns) + Postgres persistence |
| 7 | Multi-tenant | Separate apps per client (consolidate at ~10) |
| 8 | S3 export | Daily cron from Postgres → S3 |
| 9 | Auth | Username + password (per user) |
| 10 | Feedback | Thumbs up/down (Chainlit built-in) |
| 11 | Error handling | Friendly error messages for all failure modes |
| 12 | File upload | Phase 2 |
| 13 | Response formatting | Markdown + sources footer (product names, not filenames) |
| 14 | Rate limiting | Per-query $0.50 cap; per-user daily limits in Phase 2 |

---

## Open Questions (resolve during build)

1. **Chainlit + Agent SDK streaming** — Does `ClaudeSDKClient.receive_response()` yield individual tokens or full TextBlocks? Determines whether chat streams character-by-character or in bursts.

2. **Chainlit data layer for Railway Postgres** — Verify the official Chainlit Postgres data layer works with Railway's connection string format.

3. **Edit mode UI toggle** — Chainlit may not have a built-in toggle switch. May need a chat command (`/edit on`) or a custom action button.

4. **CLAUDE.md as system prompt** — Verify Agent SDK accepts a long system prompt string (CLAUDE.md is ~400 lines). May need to trim or summarize for token efficiency.

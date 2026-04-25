"""Agent SDK integration — mode switching, CLAUDE.md loading, streaming."""

import os
import logging
from pathlib import Path
from claude_code_sdk import query, ClaudeCodeOptions, ResultMessage
from claude_code_sdk.types import StreamEvent

logger = logging.getLogger(__name__)

# Monkey-patch SDK to skip unknown message types (e.g. rate_limit_event)
# instead of raising MessageParseError. Fixed upstream but not yet released.
import claude_code_sdk._internal.message_parser as _mp

_original_parse = _mp.parse_message


def _patched_parse(data):
    try:
        return _original_parse(data)
    except _mp.MessageParseError as e:
        if "Unknown message type" in str(e):
            logger.debug("Skipping unknown SDK message type: %s", data.get("type"))
            return None
        raise


_mp.parse_message = _patched_parse

# Also patch the reference in client.py since it imported parse_message directly
import claude_code_sdk._internal.client as _client
_client.parse_message = _patched_parse

READ_TOOLS = ["Read", "Glob", "Grep"]
WRITE_TOOLS = ["Read", "Glob", "Grep", "Write", "Edit"]


def sync_client_prompt(wiki_path: str, client_path: str) -> None:
    """Copy client system prompt into wiki dir so the agent sees it via CLAUDE.md."""
    src = Path(client_path, "system_prompt.md")
    dst = Path(wiki_path, "CLIENT_INSTRUCTIONS.md")
    if src.exists():
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    elif dst.exists():
        dst.unlink()


def swap_claude_md(wiki_path: str, edit_mode: bool) -> None:
    """Use slim CLAUDE_CHAT.md for read queries, full CLAUDE.md for edit mode.

    The agent reads CLAUDE.md as its system prompt from cwd. We swap the file
    so read-mode queries get a trimmed version (~1.5k tokens instead of ~4k),
    cutting per-query cost significantly.
    """
    wiki = Path(wiki_path)
    active = wiki / "CLAUDE.md"
    full = wiki / "CLAUDE_FULL.md"
    chat = wiki / "CLAUDE_CHAT.md"

    # First run: back up the full version if not already done
    if not full.exists() and active.exists():
        active.rename(full)
        # Copy chat version into place for the first read-mode query
        if chat.exists():
            active.write_text(chat.read_text(encoding="utf-8"), encoding="utf-8")

    if edit_mode:
        # Use full CLAUDE.md for edit mode (wiki management rules needed)
        if full.exists():
            active.write_text(full.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        # Use slim CLAUDE_CHAT.md for read mode
        if chat.exists():
            active.write_text(chat.read_text(encoding="utf-8"), encoding="utf-8")


async def query_agent(
    message: str,
    edit_mode: bool,
    wiki_path: str,
    client_path: str,
    session_id: str | None = None,
):
    """Stream text tokens from the Agent SDK.

    Yields text chunks as they arrive for real-time streaming in the UI.
    After all text chunks, yields a dict {"session_id": "..."} with the
    session ID for conversation resumption.
    """
    tools = WRITE_TOOLS if edit_mode else READ_TOOLS
    model = "claude-opus-4-6" if edit_mode else "claude-sonnet-4-6"
    max_turns = 15 if edit_mode else 8

    sync_client_prompt(wiki_path, client_path)
    swap_claude_md(wiki_path, edit_mode)

    options = ClaudeCodeOptions(
        allowed_tools=tools,
        cwd=wiki_path,
        model=model,
        max_turns=max_turns,
        include_partial_messages=True,
        permission_mode="bypassPermissions",
        debug_stderr=open(os.devnull, "w", encoding="utf-8"),
    )

    # Resume previous session for multi-turn conversation
    if session_id:
        options.resume = session_id

    try:
        async for msg in query(prompt=message, options=options):
            if msg is None:
                continue
            if isinstance(msg, StreamEvent):
                event = msg.event
                if event.get("type") == "content_block_delta":
                    delta = event.get("delta", {})
                    if delta.get("type") == "text_delta":
                        text = delta.get("text", "")
                        if text:
                            yield text
            elif isinstance(msg, ResultMessage):
                if msg.subtype != "success":
                    yield f"\n\n_Agent stopped: {msg.subtype}_"
                # Yield session_id for the caller to store
                sid = getattr(msg, "session_id", None)
                if sid:
                    yield {"session_id": sid}
    except Exception as e:
        if "Unknown message type" in str(e):
            logger.warning("SDK parse error (likely rate_limit_event): %s", e)
            yield "\n\n_The assistant is temporarily busy. Please try again in a moment._"
        else:
            raise

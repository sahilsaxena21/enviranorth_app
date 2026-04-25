"""Chainlit app — main entry point for the Envira-North Product Assistant."""

import chainlit as cl
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer
from dotenv import load_dotenv

load_dotenv()

from agent import query_agent
from config import get_users, get_admins, WIKI_DIR, CLIENT_DIR


# --- Data Persistence (enables thread sidebar) ---

@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(conninfo="sqlite+aiosqlite:///data/chat_history.db")


# --- Auth ---

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    users = get_users()
    if username in users and users[username] == password:
        admins = get_admins()
        role = "admin" if username in admins else "user"
        return cl.User(
            identifier=username,
            metadata={"role": role, "provider": "credentials"},
        )
    return None


# --- Starters ---

@cl.set_starters
async def starters():
    return [
        cl.Starter(
            label="Compare fan controllers",
            message="Compare the SmartAIR vs TouchAIR controllers — features, pros, and cons.",
        ),
        cl.Starter(
            label="Best fan for my space",
            message="What's the best HVLS fan for a warehouse with 25ft ceilings?",
        ),
        cl.Starter(
            label="Installation guide",
            message="Walk me through the installation process for a Sailfin fan.",
        ),
        cl.Starter(
            label="Product specs",
            message="What are the specs for the 24ft geared Sailfin?",
        ),
    ]


# --- Chat Start ---

HISTORY_WINDOW = 3

@cl.on_chat_start
async def on_start():
    cl.user_session.set("edit_mode", False)
    cl.user_session.set("msg_count", 0)


# --- Main Message Handler ---

@cl.on_message
async def on_message(message: cl.Message):
    user = cl.user_session.get("user")
    edit_mode = cl.user_session.get("edit_mode", False)

    # Handle /edit toggle command
    if message.content.strip().lower() in ("/edit on", "/edit off"):
        admins = get_admins()
        is_admin = user and user.identifier in admins
        if not is_admin:
            await cl.Message(content="Only admins can toggle edit mode.").send()
            return

        edit_mode = message.content.strip().lower() == "/edit on"
        cl.user_session.set("edit_mode", edit_mode)
        status = "enabled" if edit_mode else "disabled"
        await cl.Message(content=f"Edit mode {status}.").send()
        return

    import re

    # Rolling session window — reset after N messages to cap token costs
    msg_count = cl.user_session.get("msg_count", 0) + 1
    cl.user_session.set("msg_count", msg_count)
    session_id = cl.user_session.get("agent_session_id")
    if msg_count > HISTORY_WINDOW:
        session_id = None
        cl.user_session.set("agent_session_id", None)
        cl.user_session.set("msg_count", 1)

    # Show a temporary indicator based on mode
    indicator_text = "*Updating Knowledge Base...*" if edit_mode else "*Searching Knowledge Base...*"
    msg = cl.Message(content=indicator_text, parent_id="")
    await msg.send()

    buffer = []

    try:
        async for token in query_agent(
            message=message.content,
            edit_mode=edit_mode,
            wiki_path=str(WIKI_DIR),
            client_path=str(CLIENT_DIR),
            session_id=session_id,
        ):
            # Dict tokens carry metadata (session_id), not display text
            if isinstance(token, dict):
                if "session_id" in token:
                    cl.user_session.set("agent_session_id", token["session_id"])
                continue
            buffer.append(token)

        # Strip agent metadata lines from end of response
        full_text = "".join(buffer)
        full_text = re.sub(r"\s*Found relevant information \(\d+ chunks? streamed\)\s*$", "", full_text)
        full_text = re.sub(r"\s*Used Searching Knowledge Base[^\n]*$", "", full_text)

        # Update the same message with the final response (preserves it in data layer)
        msg.content = full_text
        await msg.update()

    except Exception as e:
        import traceback
        traceback.print_exc()
        error_type = type(e).__name__
        if "api" in error_type.lower() or "anthropic" in error_type.lower():
            await cl.Message(
                content="Our AI assistant is temporarily unavailable. Please try again in a few minutes."
            ).send()
        elif "budget" in error_type.lower():
            await cl.Message(
                content="This question required too many lookups. Please try a more specific question."
            ).send()
        else:
            await cl.Message(
                content=f"Something went wrong: `{error_type}: {e}`"
            ).send()


# --- Resume Past Conversations ---

@cl.on_chat_resume
async def on_resume(thread):
    cl.user_session.set("msg_count", 0)

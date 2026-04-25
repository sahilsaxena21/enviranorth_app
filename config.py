"""Client config loader — reads settings from env vars and client config files."""

import os
from pathlib import Path

CLIENT_NAME = os.environ.get("CLIENT_NAME", "enviranorth")
CLIENT_DIR = Path(__file__).parent / "clients" / CLIENT_NAME
WIKI_DIR = Path(__file__).parent / "wiki"


def get_users() -> dict[str, str]:
    """Parse USERS env var into {username: password} dict."""
    raw = os.environ.get("USERS", "")
    users = {}
    for pair in raw.split(","):
        pair = pair.strip()
        if ":" in pair:
            username, password = pair.split(":", 1)
            users[username.strip()] = password.strip()
    return users


def get_admins() -> set[str]:
    """Parse ADMINS env var into a set of usernames."""
    raw = os.environ.get("ADMINS", "")
    return {name.strip() for name in raw.split(",") if name.strip()}

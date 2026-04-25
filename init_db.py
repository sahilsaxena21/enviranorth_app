"""Initialize the SQLite database for Chainlit data persistence."""

import sqlite3
import os

DB_PATH = "data/chat_history.db"

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.executescript("""
CREATE TABLE IF NOT EXISTS users (
    "id"          TEXT PRIMARY KEY,
    "identifier"  TEXT NOT NULL UNIQUE,
    "createdAt"   TEXT,
    "metadata"    TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS threads (
    "id"             TEXT PRIMARY KEY,
    "name"           TEXT,
    "userId"         TEXT,
    "userIdentifier" TEXT,
    "createdAt"      TEXT,
    "tags"           TEXT,
    "metadata"       TEXT DEFAULT '{}',
    FOREIGN KEY ("userId") REFERENCES users("id")
);

CREATE TABLE IF NOT EXISTS steps (
    "id"              TEXT PRIMARY KEY,
    "name"            TEXT,
    "type"            TEXT,
    "threadId"        TEXT,
    "parentId"        TEXT,
    "streaming"       INTEGER DEFAULT 0,
    "waitForAnswer"   INTEGER DEFAULT 0,
    "isError"         INTEGER DEFAULT 0,
    "input"           TEXT,
    "output"          TEXT,
    "metadata"        TEXT DEFAULT '{}',
    "tags"            TEXT DEFAULT '[]',
    "createdAt"       TEXT,
    "start"           TEXT,
    "end"             TEXT,
    "generation"      TEXT,
    "showInput"       TEXT,
    "language"        TEXT,
    "rootRunId"       TEXT,
    FOREIGN KEY ("threadId") REFERENCES threads("id")
);

CREATE TABLE IF NOT EXISTS elements (
    "id"        TEXT PRIMARY KEY,
    "threadId"  TEXT,
    "forId"     TEXT,
    "type"      TEXT,
    "name"      TEXT,
    "display"   TEXT,
    "language"  TEXT,
    "size"      TEXT,
    "page"      INTEGER,
    "url"       TEXT,
    "objectKey" TEXT,
    "mime"      TEXT,
    "chainlitKey" TEXT,
    "props"     TEXT DEFAULT '{}',
    FOREIGN KEY ("threadId") REFERENCES threads("id")
);

CREATE TABLE IF NOT EXISTS feedbacks (
    "id"        TEXT PRIMARY KEY,
    "forId"     TEXT,
    "threadId"  TEXT,
    "value"     INTEGER,
    "comment"   TEXT,
    "strategy"  TEXT,
    FOREIGN KEY ("forId") REFERENCES steps("id")
);

CREATE INDEX IF NOT EXISTS idx_threads_user ON threads("userId");
CREATE INDEX IF NOT EXISTS idx_threads_user_ident ON threads("userIdentifier");
CREATE INDEX IF NOT EXISTS idx_steps_thread ON steps("threadId");
CREATE INDEX IF NOT EXISTS idx_elements_thread ON elements("threadId");
CREATE INDEX IF NOT EXISTS idx_feedbacks_for ON feedbacks("forId");
""")

conn.commit()
conn.close()

print(f"Database initialized at {DB_PATH}")

import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver


def build_sqlite_checkpointer(db_path: str = "sidekick_checkpoints.sqlite") -> SqliteSaver:
    # Thread-safe connection suitable for async usage
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return SqliteSaver(conn)
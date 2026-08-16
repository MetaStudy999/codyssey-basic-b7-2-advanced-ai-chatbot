import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "reference" / "database.db"

if not DB_PATH.exists():
    raise SystemExit(f"[FAIL] database not found: {DB_PATH}")

queries = {
    "users": "SELECT id, email, username, substr(password_hash, 1, 12) || '...' FROM users ORDER BY id",
    "chat_sessions": "SELECT id, user_id, title FROM chat_sessions ORDER BY id",
    "messages": "SELECT id, session_id, role, substr(content, 1, 60) FROM messages ORDER BY id",
    "posts": "SELECT id, user_id, title FROM posts ORDER BY id",
    "auth_tokens": "SELECT id, user_id, substr(token_hash, 1, 12) || '...' FROM auth_tokens ORDER BY id",
}

with sqlite3.connect(DB_PATH) as connection:
    print(f"[PASS] database: {DB_PATH}")
    for name, sql in queries.items():
        rows = connection.execute(sql).fetchall()
        print(f"[PASS] {name}: {len(rows)} row(s)")
        for row in rows[:10]:
            print("  ", row)

print("[INFO] Password/token values are intentionally shown only as truncated hashes.")

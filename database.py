import sqlite3
from datetime import datetime

DB_NAME = "tickets.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            issue_type TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            resolved_at TEXT,
            resolution_notes TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database and tables initialized successfully.")

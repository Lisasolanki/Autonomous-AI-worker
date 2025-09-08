# backend/models.py
import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS insights(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      topics TEXT,
      summary TEXT,
      recommendations TEXT,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

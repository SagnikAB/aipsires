import sqlite3
from datetime import datetime

DB_NAME = "resumes.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score INTEGER,
        skills TEXT,
        uploaded_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_resume(filename, score, skills):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO resumes (filename, score, skills, uploaded_at)
    VALUES (?, ?, ?, ?)
    """, (filename, score, ", ".join(skills), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

def get_all_resumes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resumes ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data

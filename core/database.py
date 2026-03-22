import sqlite3

def connect_db():
    return sqlite3.connect("resume.db")


def init_db():
    conn = connect_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score INTEGER,
        keywords TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_resume(filename, score, keywords):
    conn = connect_db()
    c = conn.cursor()

    c.execute(
        "INSERT INTO resumes (filename, score, keywords) VALUES (?, ?, ?)",
        (filename, score, ", ".join(keywords))
    )

    conn.commit()
    conn.close()


def get_all_resumes():
    conn = connect_db()
    c = conn.cursor()

    c.execute("SELECT filename, score, keywords FROM resumes ORDER BY id DESC")
    data = c.fetchall()

    conn.close()
    return data
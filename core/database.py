import sqlite3

def connect_db():
    return sqlite3.connect("resume.db")

def init_db():
    conn = connect_db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_score(filename, score):
    conn = connect_db()
    c = conn.cursor()

    c.execute("INSERT INTO history (filename, score) VALUES (?, ?)", (filename, score))

    conn.commit()
    conn.close()


def get_history():
    conn = connect_db()
    c = conn.cursor()

    c.execute("SELECT filename, score FROM history ORDER BY id DESC")
    data = c.fetchall()

    conn.close()
    return data
import sqlite3

def init_db():
    conn = sqlite3.connect("candidates.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS candidates(
        id INTEGER PRIMARY KEY,
        name TEXT,
        resume_score REAL,
        interview_score REAL,
        final_score REAL
    )
    """)
    conn.close()

def insert_candidate(name, r_score, i_score):
    final = r_score*0.6 + i_score*0.4
    conn = sqlite3.connect("candidates.db")
    conn.execute(
      "INSERT INTO candidates(name,resume_score,interview_score,final_score) VALUES(?,?,?,?)",
      (name, r_score, i_score, final)
    )
    conn.commit()
    conn.close()

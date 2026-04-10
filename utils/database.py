import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        owner TEXT,
        stars INTEGER,
        forks INTEGER,
        issues INTEGER,
        score REAL,
        url TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()


def insert_project(p):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO projects 
        (name, owner, stars, forks, issues, score, url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            p['name'],
            p['owner'],
            p['stars'],
            p['forks'],
            p['issues'],
            p['score'],
            p['url']
        ))

        conn.commit()
        conn.close()
    except:
        pass
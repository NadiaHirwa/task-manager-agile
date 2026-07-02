import sqlite3
from turtle import title

DB_NAME = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    
def add_task(title):
    if not title or not title.strip():
        return None

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (title, 0)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "title": title, "completed": False}

def get_all_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, completed FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "completed": bool(row[2])
        })
    return tasks

def mark_complete(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    existing = cursor.fetchone()

    if existing is None:
        conn.close()
        return False

    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return True
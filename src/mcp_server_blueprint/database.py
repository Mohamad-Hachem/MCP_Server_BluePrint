import sqlite3
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "data"
db_path = data_dir / "tasks.db"

def init_db() -> None:

    data_dir.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL DEFAULT 'medium',
                status TEXT NOT NULL DEFAULT 'todo'
            )
        """)

        conn.commit()
    finally:
        conn.close()


def save_task(task:dict) -> None:

    conn = sqlite3.connect(db_path)

    try:
        conn.execute(
            """
            INSERT INTO tasks (
                task_id, title, description, priority, status
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                task["task_id"],
                task["title"],
                task["description"],
                task["priority"],
                task["status"],
            )
        )

        conn.commit()
    finally:
        conn.close()


def get_all_tasks() -> list[dict]:

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    try:
        
        cur.execute('SELECT * FROM tasks;')
        rows = cur.fetchall()
    finally:
        conn.close()

    return [dict(row) for row in rows]

if __name__ == "__main__":
    init_db()
    print(get_all_tasks())
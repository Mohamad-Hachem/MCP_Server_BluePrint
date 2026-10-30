import sqlite3
from pathlib import Path


def init_db() -> None:
    # 1. Determine the project root
    project_root = Path(__file__).resolve().parents[2]

    # 2. Create the data directory
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # 3. Connect to the SQLite database
    db_path = data_dir / "tasks.db"
    conn = sqlite3.connect(db_path)

    try:
        # 4. Create the tasks table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL DEFAULT 'medium',
                status TEXT NOT NULL DEFAULT 'todo'
            )
        """)

        # 5. Commit the changes
        conn.commit()
    finally:
        # Close the connection even if an error occurs
        conn.close()


def save_task(task:dict) -> None:
    # 1. Determine the project root
    project_root = Path(__file__).resolve().parents[2]

    # 2. Create the data directory
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # 3. Connect to the SQLite database
    db_path = data_dir / "tasks.db"
    conn = sqlite3.connect(db_path)

    try:
        # 4. Create the tasks table
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

        # 5. Commit the changes
        conn.commit()
    finally:
        # Close the connection even if an error occurs
        conn.close()

if __name__ == "__main__":
    init_db()
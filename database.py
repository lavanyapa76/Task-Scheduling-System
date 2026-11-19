import sqlite3

DB_NAME = "tasks.db"

def connect():
    return sqlite3.connect(DB_NAME, timeout=10)

def init_db():
    with connect() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending',
                worker TEXT DEFAULT '-',
                result TEXT DEFAULT '-'
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS workers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Idle'
            )
        """)
        for i in range(1, 4):
            con.execute(
                "INSERT OR IGNORE INTO workers (id, name, status) VALUES (?, ?, 'Idle')",
                (i, f"Worker {i}")
            )

def add_task(name):
    with connect() as con:
        con.execute("INSERT INTO tasks (name) VALUES (?)", (name,))

def get_tasks():
    with connect() as con:
        return con.execute(
            "SELECT id, name, status, worker, result FROM tasks ORDER BY id DESC"
        ).fetchall()

def get_workers():
    with connect() as con:
        return con.execute("SELECT name, status FROM workers ORDER BY id").fetchall()

def get_pending_task():
    with connect() as con:
        return con.execute(
            "SELECT id, name FROM tasks WHERE status='Pending' ORDER BY id LIMIT 1"
        ).fetchone()

def update_task(task_id, status, worker, result):
    with connect() as con:
        con.execute(
            "UPDATE tasks SET status=?, worker=?, result=? WHERE id=?",
            (status, worker, result, task_id)
        )

def update_worker(worker_id, status):
    with connect() as con:
        con.execute("UPDATE workers SET status=? WHERE id=?", (status, worker_id))

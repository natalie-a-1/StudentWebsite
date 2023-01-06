import sqlite3


def get_todo_tasks():
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        )
    ''')
    cursor.execute('''
        SELECT id, title, completed FROM tasks
    ''')
    tasks = cursor.fetchall()
    conn.commit()
    conn.close()
    return tasks


def add_todo_tasks(title, completed):
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, completed) VALUES (?, ?)
    ''', (title, completed))
    conn.commit()
    conn.close()

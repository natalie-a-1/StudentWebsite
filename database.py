import sqlite3


def get_todo_tasks():
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        SELECT id, title FROM tasks
    ''')
    tasks = cursor.fetchall()
    conn.commit()
    conn.close()
    return tasks


def add_todo_tasks(title):
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title) VALUES (?)
    ''', [title])
    conn.commit()
    conn.close()


def delete_todo_tasks(title):
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    # cursor.execute('''
    #     DELETE FROM tasks WHERE title=
    # ''')
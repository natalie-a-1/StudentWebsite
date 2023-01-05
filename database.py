import sqlite3


def get_todo_items():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, title, completed FROM items
    ''')
    items = cursor.fetchall()
    conn.close()
    return items


def add_todo_item(title, completed):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO items (title, completed) VALUES (?, ?)
    ''', (title, completed))
    conn.commit()
    conn.close()

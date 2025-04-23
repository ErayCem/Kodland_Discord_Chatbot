import sqlite3

def create_connection(db_path='tasks.db'):
    """Veritabanına bağlanıyoruz"""
    return sqlite3.connect(db_path)

def create_table(conn=None):
    """Görevler tablosunu oluşturuyoruz"""
    if conn is None:
        conn = create_connection()
        should_close = True
    else:
        should_close = False

    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        is_completed BOOLEAN NOT NULL CHECK (is_completed IN (0, 1))
    )
    ''')

    conn.commit()
    if should_close:
        conn.close()

def add_task(description, conn=None):
    if conn is None:
        conn = create_connection()
        should_close = True
    else:
        should_close = False

    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description, is_completed) VALUES (?, ?)', (description, 0))
    conn.commit()
    if should_close:
        conn.close()

def delete_task(task_id, conn=None):
    if conn is None:
        conn = create_connection()
        should_close = True
    else:
        should_close = False

    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    if should_close:
        conn.close()

def get_all_tasks(conn=None):
    if conn is None:
        conn = create_connection()
        should_close = True
    else:
        should_close = False

    cursor = conn.cursor()
    cursor.execute('SELECT id, description, is_completed FROM tasks')
    tasks = cursor.fetchall()
    if should_close:
        conn.close()
    return tasks

def complete_task(task_id, conn=None):
    if conn is None:
        conn = create_connection()
        should_close = True
    else:
        should_close = False

    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET is_completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    if should_close:
        conn.close()

# Gerçek veritabanında tabloyu oluşturuyoruz
if __name__ == '__main__':
    conn = create_connection()
    create_table(conn)
    conn.close()

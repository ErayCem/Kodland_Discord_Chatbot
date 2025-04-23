import unittest
import sqlite3
from database import add_task, delete_task

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                is_completed INTEGER DEFAULT 0
                            )''')
        add_task("Silinecek Görev", conn=self.conn)

    def test_delete_task(self):
        delete_task(1, conn=self.conn)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = 1")
        task = cursor.fetchone()
        self.assertIsNone(task)

if __name__ == '__main__':
    unittest.main()

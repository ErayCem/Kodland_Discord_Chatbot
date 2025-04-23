
import unittest
import sqlite3
from database import add_task

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                is_completed INTEGER DEFAULT 0
                            )''')
        self.conn.commit()

    def test_add_task(self):
        add_task("Test Görev", conn=self.conn)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test Görev")

if __name__ == '__main__':
    unittest.main()

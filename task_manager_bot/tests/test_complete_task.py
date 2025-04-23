import unittest
import sqlite3
from database import add_task, complete_task

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                is_completed INTEGER DEFAULT 0
                            )''')
        add_task("Tamamlanacak Görev", conn=self.conn)

    def test_complete_task(self):
        complete_task(1, conn=self.conn)
        cursor = self.conn.cursor()
        cursor.execute("SELECT is_completed FROM tasks WHERE id = 1")
        is_completed = cursor.fetchone()[0]
        self.assertEqual(is_completed, 1)

if __name__ == '__main__':
    unittest.main()

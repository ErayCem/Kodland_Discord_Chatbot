import unittest
import sqlite3
from database import add_task, get_all_tasks

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT NOT NULL,
                                is_completed INTEGER DEFAULT 0
                            )''')
        add_task("Görev 1", conn=self.conn)
        add_task("Görev 2", conn=self.conn)

    def test_show_tasks(self):
        tasks = get_all_tasks(conn=self.conn)
        self.assertEqual(len(tasks), 2)

if __name__ == '__main__':
    unittest.main()

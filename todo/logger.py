
from db import DataBase
class Logger:
    def __init__(self, data):
        self.data = data

    def log_action(self, user_id, action, todo_id=None):

        with DataBase(self.data) as cur:
            cur.execute("""
                INSERT INTO logs (user_id, action, todo_id)
                VALUES (%s, %s, %s);
            """, (user_id, action, todo_id))

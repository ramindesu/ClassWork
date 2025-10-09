import requests
from db import DataBase
API_URL = "https://httpbin.org/post"
class Logger:
    def __init__(self, data):
        self.data = data

    def log_action(self, user_id, action, todo_id=None):

        with DataBase(self.data) as cur:
            cur.execute("""
                INSERT INTO logs (user_id, action, todo_id)
                VALUES (%s, %s, %s);
            """, (user_id, action, todo_id))
        data = {"user_id": user_id, "action": action, "todo_id": todo_id}
        try:
            r = requests.post(API_URL, json=data)
            print(f" Log sent to API ({r.status_code})")
        except Exception as e:
            print(" Failed to send log:", e)

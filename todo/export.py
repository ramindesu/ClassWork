import json

from db import DataBase

class Logger:
    def __init__(self, data, filename="logs.json"):
        self.data = data
        self.file = filename

       
        if not self.file.exists():
            with open(self.file, "w") as f:
                json.dump([], f)

    def log_action(self, user_id, action, todo_id=None):

        with DataBase(self.data) as cur:
            cur.execute("""
                INSERT INTO logs (user_id, action, todo_id)
                VALUES (%s, %s, %s);
            """, (user_id, action, todo_id))


        new_log = {
            "user_id": user_id,
            "action": action,
            "todo_id": todo_id
        }

        with open(self.file, "r+") as f:
            logs = json.load(f)   
            logs.append(new_log)      
            json.dump(logs, f, indent=4)
        print(f"log saved: {new_log}")
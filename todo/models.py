from db import DataBase
from logger import Logger

class TodoService:
    def __init__(self, data):
        self.data = data
        self.logger = Logger(data)

    def create_tables(self):
        with DataBase(self.data) as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id) ON DELETE CASCADE,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                due_time TIMESTAMP,
                status VARCHAR(10) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(id) ON DELETE CASCADE,
                action VARCHAR(50),
                todo_id INT REFERENCES todos(id) ON DELETE CASCADE,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
        print(" Tables created successfully")
    def add_todo(self,user_id,title,descrption,due_time):
        with DataBase(self.data) as cur:
            cur.execute(f'insert into todos (user_id,title,description,due_time) values ({user_id},{title},{descrption},{due_time})') 
            todo_id = cur.fetchone()[0]

        self.logger.log_action(user_id,'add task', todo_id)
        return todo_id
    

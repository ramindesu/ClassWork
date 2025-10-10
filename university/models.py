from db import DataBase

class TodoService:
    def __init__(self, data):
        self.data = data

    def create_tables(self):
        with DataBase(self.data) as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    birth_year INT
                );
            """)


            cur.execute("""
                CREATE TABLE IF NOT EXISTS department (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL
                );
            """)


            cur.execute("""
                CREATE TABLE IF NOT EXISTS master (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL,
                    field VARCHAR(100) NOT NULL,
                    department_id INT UNIQUE REFERENCES department(id) ON DELETE CASCADE
                );
            """)


            cur.execute("""
                CREATE TABLE IF NOT EXISTS major (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    credit INT,
                    master_id INT REFERENCES master(id) ON DELETE SET NULL
                );
            """)


            cur.execute("""
                CREATE TABLE IF NOT EXISTS enrollments (
                    id SERIAL PRIMARY KEY,
                    student_id INT REFERENCES student(id) ON DELETE CASCADE,
                    major_id INT REFERENCES major(id) ON DELETE CASCADE,
                    enrollment_date DATE DEFAULT CURRENT_DATE
                );
            """)

        print("Tables created successfully")
    def queryes(self,query):
        with DataBase(self.data) as cur:
            cur.execute(query)
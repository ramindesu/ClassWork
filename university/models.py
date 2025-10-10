from db import DataBase


class UniService:
    def __init__(self, data):
        self.data = data

    def create_tables(self):
        with DataBase(self.data) as cur:

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS student (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    birth_year INT
                );
            """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS department (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL
                );
            """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS master (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(60) NOT NULL,
                    field VARCHAR(100) NOT NULL,
                    department_id INT  REFERENCES department(id) ON DELETE CASCADE
                );
            """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS major (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100) NOT NULL,
                    credit INT,
                    master_id INT REFERENCES master(id) ON DELETE SET NULL
                );
            """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS enrollments (
                    id SERIAL PRIMARY KEY,
                    student_id INT REFERENCES student(id) ON DELETE CASCADE,
                    major_id INT REFERENCES major(id) ON DELETE CASCADE,
                    enrollment_date DATE DEFAULT CURRENT_DATE
                );
            """
            )

        print("Tables created successfully")

    def list(self, table):
        with DataBase(self.data) as cur:
            cur.execute(f"SELECT * FROM {table}")
            return cur.fetchall()

    def add_email(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
            ALTER TABLE student
            ADD COLUMN IF NOT EXISTS email VARCHAR(255);
        """
            )
        print("Email column added (if it didn't exist)")

    def queryes(self, query):
        with DataBase(self.data) as cur:
            cur.execute(query)

    def remove_master_field(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
            ALTER TABLE master
            DROP COLUMN IF EXISTS field;
        """
            )
            print("Column 'field' removed from master table (if it existed)")

    def list_majors(self):
        with DataBase(self.data) as cur:
            cur.execute("SELECT * FROM major")
            return cur.fetchall()

    def list_students_by_age(self):
        """
        نمایش همه دانشجوها از پیر به جوان
        """
        with DataBase(self.data) as cur:
            cur.execute(
                """
            SELECT * FROM student
            ORDER BY birth_year ASC
        """
            )
            return cur.fetchall()

    def count_students_per_major(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
                SELECT m.title, COUNT(e.student_id) as student_count
                FROM major m
                LEFT JOIN enrollments e ON m.id = e.major_id
                GROUP BY m.title
            """
            )
            return cur.fetchall()

    def majors_with_more_than_3_students(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
                SELECT m.title, COUNT(e.student_id) as student_count
                FROM major m
                JOIN enrollments e ON m.id = e.major_id
                GROUP BY m.title
                HAVING COUNT(e.student_id) > 3
            """
            )
            return cur.fetchall()

    def make_major_title_not_null(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
                ALTER TABLE major
                ALTER COLUMN title SET NOT NULL
            """
            )

    def set_default_master_field(self):
        with DataBase(self.data) as cur:
            cur.execute(
                """
                ALTER TABLE master
                ALTER COLUMN field SET DEFAULT 'General'
            """
            )


def oldest_and_youngest_student_union(self):
    with DataBase(self.data) as cur:
        cur.execute(
            """
            SELECT 'oldest' AS type, *
            FROM student
            ORDER BY birth_year ASC
            LIMIT 1
            UNION ALL
            SELECT 'youngest' AS type, *
            FROM student
            ORDER BY birth_year DESC
            LIMIT 1
        """
        )
        return cur.fetchall()

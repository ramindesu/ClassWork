import  psycopg

class DataBase:
    def __init__(self,data):
        """
        data = "dbname=todo_app user=postgres password=shir8844 host=localhost port=5432
        """
        self.data = data
        self.con = ''
        self.cur = '' 
    def __enter__(self):
        self.con = psycopg.connect(self.data)
        self.cur = self.con.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:  
            self.con.rollback()
            print(" error :", exc_val)
        else:
            self.con.commit()
        self.cur.close()
        self.con.close()


        
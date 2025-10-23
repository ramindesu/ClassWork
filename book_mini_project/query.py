from db import Database
from models import *
dsn = 'dbname=lib user=postgres password=shir884 host=localhost '

class Query:
    def __init__(self, dsn):
        self.dsn = dsn

    def create_table(self):
        with Database(self.dsn) as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS book (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(60),
                    author VARCHAR(60),
                    isbn INT UNIQUE,
                    is_read BOOLEAN DEFAULT FALSE
                );
            """)
        print(" Table created successfully.")

    def insert_book(self, title, author, isbn, is_read=False):
        with Database(self.dsn) as cur:
            cur.execute("""
                INSERT INTO book (title, author, isbn, is_read)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (title, author, isbn, is_read))
            book_id = cur.fetchone()[0]
        print(f" Book '{title}' added with id {book_id}.")
        return book_id

    def get_all_books(self):
        with Database(self.dsn) as cur:
            cur.execute("SELECT * FROM book;")
            books = cur.fetchall()
        if not books:
                raise ValueError("books is not found")
        else:
            print(" All books:")
            for book in books:
                print(book)
        return books

    def delete_book(self, book_id):
        with Database(self.dsn) as cur:
            cur.execute("DELETE FROM book WHERE id = %s RETURNING id;", (book_id,))
            deleted = cur.fetchone()
        if deleted:
            print(f" Book with id {book_id} deleted.")
        else:
            print(f" No book found with id {book_id}.")

    def update_book(self, book_id, title=None, author=None, isbn=None, is_read=None):

        updates = []
        values = []

        if title:
            updates.append("title = %s")
            values.append(title)
        if author:
            updates.append("author = %s")
            values.append(author)
        if isbn:
            updates.append("isbn = %s")
            values.append(isbn)
        if is_read is not None:
            updates.append("is_read = %s")
            values.append(is_read)

        if not updates:
            print(" Nothing to update.")
            return

        values.append(book_id)
        query = f"UPDATE book SET {', '.join(updates)} WHERE id = %s RETURNING id;"

        with Database(self.dsn) as cur:
            cur.execute(query, tuple(values))
            updated = cur.fetchone()
        if updated:
            print(f" Book with id {book_id} updated successfully.")
        else:
            print(f" No book found with id {book_id}.")

    def search_book(self, atr):

        with Database(self.dsn) as cur:
            if atr.isdigit():

                cur.execute("SELECT * FROM book WHERE isbn = %s;", (int(atr),))
            else:

                cur.execute("""
                    SELECT * FROM book
                    WHERE LOWER(title) LIKE LOWER(%s)
                       OR LOWER(author) LIKE LOWER(%s);
                """, (f"%{atr}%", f"%{atr}%"))

            results = cur.fetchall()

        if not results:
            print(f" No books found matching '{atr}'.")
        else:
            print(f" Search results for '{atr}':")
            for book in results:
                print(book)
        return results
from models import *
from query import *
from db import *
import argparse

# اتصال دیتابیس
dsn = 'dbname=lib user=postgres password=shir884 host=localhost'
query = Query(dsn)

# ---- ARGPARSE ----
parser = argparse.ArgumentParser(description="Book Management System")
parser.add_argument('command', choices=['add', 'delete', 'update', 'list', 'search'], help="Choose an operation")

parser.add_argument('--title', help="Book title")
parser.add_argument('--author', help="Book author")
parser.add_argument('--isbn', type=int, help="Book ISBN number")
parser.add_argument('--read', choices=['True', 'False'], help="Mark book as read/unread")
parser.add_argument('--book_id', type=int, help="Book ID (for update/delete)")
parser.add_argument('--attr', help="Text or number to search for a book")

args = parser.parse_args()

# ---- COMMANDS ----
if args.command == 'add':
    if not (args.title and args.author and args.isbn):
        print(" Missing required arguments: --title, --author, --isbn")
    else:
        is_read = args.read == 'True' if args.read else False
        book = Book(args.title, args.author, args.isbn, is_read)
        query.insert_book(book.title, book.author, book.isbn, book.read)
        print(" Book inserted successfully.")

elif args.command == 'list':
    query.get_all_books()

elif args.command == 'delete':
    if not args.book_id:
        print(" You must provide --book_id to delete a book.")
    else:
        query.delete_book(args.book_id)

elif args.command == 'update':
    if not args.book_id:
        print(" You must provide --book_id for update.")
    else:
        is_read = None
        if args.read:
            is_read = True if args.read == 'True' else False

        query.update_book(
            book_id=args.book_id,
            title=args.title,
            author=args.author,
            isbn=args.isbn,
            is_read=is_read
        )

elif args.command == 'search':
    if not args.attr:
        print(" Please enter --attr for searching (title, author, or isbn).")
    else:
        query.search_book(args.attr)

else:
    print("not found.")
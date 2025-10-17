import json


class Book:
    def __init__(self, title: str, author: str, isbn: int, read: bool = False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.read = read

    def read_book(self):
        self.read = True
        return f"The book '{self.title}' has been read."

    def i_want_it_in_json(self):
        json_file = {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "read": self.read,
        }
        return json.dumps(json_file)

    def updatintg(self, attribiute, value):
        if attribiute not in ("title", "author", "isbn", "read"):
            return "You can’t update this attribute."
        setattr(self, attribiute, value)
        return f"{attribiute} has been updated to {value}."

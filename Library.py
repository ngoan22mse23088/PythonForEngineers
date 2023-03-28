import json
from Book import Book

class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                books = json.load(file)
        except FileNotFoundError:
            books = []
        return [Book(**book) for book in books]

    def save_books(self):
        with open(self.filename, 'w') as file:
            books = [book.__dict__ for book in self.books]
            json.dump(books, file)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def edit_book(self, index, **kwargs):
        for key, value in kwargs.items():
            setattr(self.books[index], key, value)
        self.save_books()

    def delete_book(self, index):
        del self.books[index]
        self.save_books()

    def search_book(self, search_text):
        return [book for book in self.books if search_text.lower() in book.title.lower() or search_text.lower() in book.author.lower()]

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for i, book in enumerate(self.books):
                print(f"{i + 1}. {book.title} by {book.author}, published by {book.publisher} in {book.year}, {book.quantity} copies.")
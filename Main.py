from Library import Library
from Book import Book

library = Library("books.json")

while True:
    print("""
    Menu:
    1. Add book
    2. Edit book
    3. Delete book
    4. Search book
    5. Display books
    6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        publisher = input("Enter publisher: ")
        year = input("Enter year of publication: ")
        quantity = input("Enter quantity: ")
        book = Book(title, author, publisher, year, quantity)
        library.add_book(book)
        print("Book added.")
    elif choice == "2":
        index = int(input("Enter book index: ")) - 1
        book = library.books[index]
        print(f"Editing book: {book.title}")
        title = input(f"Enter new title ({book.title}): ") or book.title
        author = input(f"Enter new author ({book.author}): ") or book.author
        publisher = input(f"Enter new publisher ({book.publisher}): ") or book.publisher
        year = input(f"Enter new year of publication ({book.year}): ") or book.year
        quantity = input(f"Enter new quantity ({book.quantity}): ") or book.quantity
        library.edit_book(index, title=title, author=author, publisher=publisher, year=year, quantity=quantity)
        print("Book edited.")
    elif choice == "3":
        index = int(input("Enter book index: ")) - 1
        book = library.books[index]
        print(f"Deleting book: {book.title}")
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == "y":
            library.delete_book(index)
            print("Book deleted.")
    elif choice == "4":
        search_text = input("Enter search text: ")
        results = library.search_book(search_text)
        if results:
            print("Search results:")
            for i, book in enumerate(results):
                print(f"{i + 1}. {book.title} by {book.author}, published by {book.publisher} in {book.year}, {book.quantity} copies.")
        else:
            print("No results.")
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

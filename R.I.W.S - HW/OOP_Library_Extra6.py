class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Successfully borrowed {self.title} written by {self.author} in {self.year}!")
        else:
            print(f"Unfortunately {self.title} by {self.author} is already borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(f"Successfully returned {self.title} by {self.author}!")


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} was successfully added!")


    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("List of books in library:")
            for book in self.books:
                status = "available" if not book.is_borrowed else "borrowed"
                print(f"- {book.title} by {book.author} ({book.year}) - {status}")


    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

#Zadání:
#Zobrazit všechny knihy
#Vypůjčit knihu
#Vrátit knihu
#Přidat knihu
#Konec
#Orwell = Book("1984", "George Orwell", 1949)
#Rowling = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997)
#Pratchett = Book("Discworld", "Terry Pratchett", 1983)


def library_menu():
    library = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Display all books")
        print("2. Borrow book")
        print("3. Return book")
        print("4. Add a new book")
        print("5. Leave")

        choice = input("Choose: ")

        if choice == "1":
            library.list_books()
        elif choice == "2":
            title = input("Type the title of the book you want to borrow: ")
            book = library.find_book(title)
            if book:
                book.borrow()
            else:
                print(f"Book with the title '{title}' wasn't found.")
        elif choice == "3":
            title = input("Type the title of the book you want to return: ")
            book = library.find_book(title)
            if book:
                book.return_book()
            else:
                print(f"Book '{title}' was not found.")
        elif choice == "4":
            title = input("Type the title of the book (case sensitive): ")
            author = input("Type the author of the book (case sensitive): ")
            year = input("Type the year the book was written: ")
            try:
                year = int(year)
                new_book = Book(title, author, year)
                library.add_book(new_book)
            except ValueError:
                print("Year is supposed to be a number.")
        elif choice == "5":
            print("Goodbye, have a great day!")
            break
        else:
            print("Wrong choice, try again!")


#Cool thing - IF its run as a script directly (not imported), program stars and initializes menu
if __name__ == "__main__":
    library_menu()

'''
library = Library()

Orwell = Book("1984", "George Orwell", 1949)
Rowling = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997)
Pratchett = Book("Discworld", "Terry Pratchett", 1983)

library.list_books()

library.add_book(Orwell)
library.add_book(Rowling)
library.add_book(Pratchett)

library.list_books()

book_to_borrow = library.find_book("1984")
if book_to_borrow:
    book_to_borrow.borrow()

library.list_books()

book_to_borrow.return_book()
library.list_books()
'''

# Base class - Book
class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance with title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the Book instance.
        """
        return f"Book: {self.title} by {self.author}"

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance with title, author, and file size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the EBook instance, including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance with title, author, and page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the PrintBook instance, including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library class
class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book (Book, EBook, or PrintBook) to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            print(book)

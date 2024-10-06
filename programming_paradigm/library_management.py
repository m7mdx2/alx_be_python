class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out
    
    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # The book is already checked out
    
    def return_book(self):
        """Mark the book as available if it is checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # The book was not checked out
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """Represents a library that holds books."""
    
    def __init__(self):
        self._books = []  # Private list to store book instances
    
    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available.")
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                return
        print(f"Sorry, '{title}' was not checked out.")
    
    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

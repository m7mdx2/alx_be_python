class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a book instance with title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to handle the deletion of a book instance. Prints a message when an object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book object in a human-readable format.
        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the book object.
        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

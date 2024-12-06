# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.pages = pages  # Number of pages in the book

    def display_info(self):
        """Display information about the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Inherited class: EBook (subclass of Book)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call the parent constructor
        self.file_size = file_size  # Additional attribute for EBook

    def display_info(self):
        """Override display_info to include file size."""
        super().display_info()  # Call the parent method to print common info
        print(f"File Size: {self.file_size} MB")

# Create objects of Book and EBook
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
ebook1 = EBook("Digital Fortress", "Dan Brown", 350, 5)

# Display the information of both books
print("Book 1 Information:")
book1.display_info()

print("\nEBook 1 Information:")
ebook1.display_info()

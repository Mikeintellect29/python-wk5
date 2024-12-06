Description
This Python program demonstrates the creation of a simple Book class and its extension using inheritance. The Book class represents a traditional book with basic attributes such as title, author, and number of pages. The EBook subclass inherits from Book and adds additional functionality, such as tracking the file size for digital books.

Features
Book Class:

Represents a traditional book with attributes like title, author, and pages.
Contains a method display_info() to print the book's details.
EBook Class:

Inherits from the Book class.
Adds a new attribute file_size for digital books (measured in MB).
Overrides the display_info() method to include the file size.
Object Creation:

Creates instances of both the Book and EBook classes to demonstrate inheritance and method overriding.

How to Use
Run the Python script in a Python environment.
The program will display the information for a traditional book and an eBook.
The EBook subclass includes an additional file size attribute, which is printed when display_info() is called.

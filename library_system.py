# library_system.py


class Book:
    def read(self):
        print("Reading a physical book.")

class DigitalBook(Book):
    def read(self):  # Overriding
        print("Reading a digital book on an e-reader.")

# Method Overloading 
class Library:
    def search(self, title=None, author=None):
        if title and author:
            print(f"Searching for '{title}' by {author}")
        elif title:
            print(f"Searching for '{title}'")
        else:
            print("Please provide search criteria.")

# MRO Example
class Downloadable:
    def access(self):
        print("Downloading content...")

class Readable:
    def access(self):
        print("Opening content to read...")

class Ebook(Downloadable, Readable):  # Multiple inheritance
    pass


if __name__ == "__main__":
    print("Method Overriding:")
    book = Book()
    digital = DigitalBook()
    book.read()         
    digital.read()     
    
    print("\nMethod Overloading:")
    lib = Library()
    lib.search("Python 101")
    lib.search("Python 101", "Noela Ankunda")

    print("\nMethod Resolution Order (MRO):")
    ebook = Ebook()
    ebook.access()     #Downloadable is before Readable 
    print(Ebook.__mro__)

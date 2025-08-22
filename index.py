# Activity 1: Design Your Own Class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Inheritance: EBook extends Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB)...")

    # Encapsulation: private attribute
    def __str__(self):
        return f"{self.info()} [EBook, {self.file_size}MB]"

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Test code
if __name__ == "__main__":
    # Activity 1
    book1 = Book("1984", "George Orwell", 328)
    ebook1 = EBook("Python 101", "Michael Driscoll", 250, 5)
    book1.read()
    print(book1.info())
    ebook1.read()
    ebook1.download()
    print(ebook1)

    # Activity 2
    vehicles = [Car(), Plane()]
    for v in vehicles:
        v.move()
" == Library Management System =="


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


class User:

    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"{self.name} cannot borrow more than {self.max_books} books.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")

    def display_borrowed_books(self):
        print(f"{self.name} has borrowed {len(self.borrowed_books)} book(s):")
        for book in self.borrowed_books:
            print(f"  - {book.title} by {book.author}")




class Student(User):
    def __init__(self,name):
        super().__init__(name,max_books = 3)

    def borrow_book(self, book):
        print(f"[Student Borrowing] {self.name} trying to borrow '{book.title}'")
        super().borrow_book(book)


class Faculty(User):
    def __init__(self,name):
        super().__init__(name,max_books=5)

    def borrow_book(self, book):
        print(f"[Faculty Borrowing] {self.name} trying to borrow '{book.title}'")
        super().borrow_book(book)

# === Example Usage ===

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Catcher in the Rye", "J.D. Salinger")

# Create a student and a faculty member
student = Student("Alice")
faculty = Faculty("Dr. Smith")

# Student borrows books
student.borrow_book(book1)
student.borrow_book(book2)
student.borrow_book(book3)
student.borrow_book(book4)

# Faculty borrows books
faculty.borrow_book(book1)
faculty.borrow_book(book2)
faculty.borrow_book(book3)
faculty.borrow_book(book4)

# Display borrowed books
print("\n--- Borrowed Books ---")
student.display_borrowed_books()
faculty.display_borrowed_books()


# Return books
student.return_book(book2)
faculty.return_book(book3)
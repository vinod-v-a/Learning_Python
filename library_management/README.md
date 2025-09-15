
---

LIBRARY MANAGEMENT SYSTEM (PYTHON + MYSQL)

---

A simple command-line based Library Management System built using Python and MySQL.
This system allows an admin to manage books, members, and issue/return operations.

---

## FEATURES

* Book Management: Add, View, Update, Delete, Search books
* Member Management: Add, View, Update, Delete members
* Transactions: Issue books, Return books, View transaction history
* Reports: View all issued books, returned books, available books

---

## REQUIREMENTS

* Python 3.6+
* MySQL Server 5.7+
* pip (Python package manager)
* mysql-connector-python (install using: pip install mysql-connector-python)

---

## FOLDER STRUCTURE

library\_management/
db\_config.py        -> Database connection setup
books.py            -> Book management module
members.py          -> Member management module
issue\_return.py     -> Issue and return module
main.py             -> Entry point (Main menu)
setup.sql           -> SQL script to create database and tables
README.txt          -> Documentation

---

## SETUP INSTRUCTIONS

1. Create Database and Tables:
   Run inside MySQL:
   mysql -u root -p < setup.sql

2. Configure Database Connection:
   Edit db\_config.py with your MySQL username and password:
   def get\_connection():
   return mysql.connector.connect(
   host="localhost",
   user="root",
   password="your\_password",
   database="library\_db"
   )

3. Run the System:
   python main.py

---

## USAGE WALKTHROUGH

When you run "python main.py" you will see:

\========== Library Management System ==========

1. Manage Books
2. Manage Members
3. Issue/Return Books
4. Exit
   \==============================================
   Enter your choice:

BOOK MANAGEMENT MENU

1. Add Book
2. View All Books
3. Update Book
4. Delete Book
5. Search Book
6. Back to Main Menu

Example:
Enter book title: Atomic Habits
Enter author name: James Clear
Enter total copies: 5
Book added successfully

View Books Example:
ID: 1, Title: Atomic Habits, Author: James Clear, Total: 5, Available: 5

MEMBER MANAGEMENT MENU

1. Add Member
2. View All Members
3. Update Member
4. Delete Member
5. Back to Main Menu

Example:
Enter member name: Vinod
Enter email: [vinod@example.com](mailto:vinod@example.com)
Member added successfully

View Members Example:
ID: 1, Name: Vinod, Email: [vinod@example.com](mailto:vinod@example.com), Joined: 2025-09-08

ISSUE AND RETURN MENU

1. Issue Book
2. Return Book
3. View All Transactions
4. Back to Main Menu

Example Issue:
Enter Member ID: 1
Enter Book ID: 1
Book issued successfully

Transactions Example:
Txn ID: 1, Member: Vinod, Book: Atomic Habits, Issue Date: 2025-09-08, Return Date: None

Return Example:
Enter Transaction ID: 1
Book returned successfully

After Return:
Txn ID: 1, Member: Vinod, Book: Atomic Habits, Issue Date: 2025-09-08, Return Date: 2025-09-08

---

## NOTES

* Handles invalid inputs and database errors gracefully
* Data is stored in MySQL (library\_db)
* Extendable for overdue tracking, audit logs, etc.
* Single admin user (no login required)

---

## SUCCESS CRITERIA

* Run using python main.py
* All data persists in MySQL
* Add, view, update, delete works for books and members
* Issue and return cycle works properly
* User-friendly menu navigation

---

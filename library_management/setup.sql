-- Create Database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- Create Books Table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    total_copies INT NOT NULL CHECK (total_copies > 0),
    available_copies INT NOT NULL CHECK (available_copies >= 0)
);

-- Create Members Table
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    join_date DATE NOT NULL
);

-- Create Issued Books Table
CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Insert Sample Books (Optional)
INSERT INTO books (title, author, total_copies, available_copies) VALUES
('Python Basics', 'John Doe', 5, 5),
('Data Science 101', 'Jane Smith', 3, 3),
('Database Systems', 'C. J. Date', 4, 4);

-- Insert Sample Members (Optional)
INSERT INTO members (name, email, join_date) VALUES
('Alice Johnson', 'alice@example.com', CURDATE()),
('Bob Williams', 'bob@example.com', CURDATE());


USE library_db;
SHOW TABLES;
SELECT * FROM books;
SELECT * FROM members;

"logic for managing books"

from db_config import get_connection


def add_book():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        total_copies = int(input("Enter total copies: "))

        available_copies = total_copies  # initially same as total

        cursor = conn.cursor()
        query = """INSERT INTO books (title, author, total_copies, available_copies) 
                   VALUES (%s, %s, %s, %s)"""
        values = (title, author, total_copies, available_copies)
        cursor.execute(query, values)
        conn.commit()
        print("✅ Book added successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def view_books():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        if not rows:
            print("\n📭 No books found in library.")
            return
        print("\n📚 All Books in Library:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, "
                  f"Total: {row[3]}, Available: {row[4]}")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def update_book():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        book_id = int(input("Enter Book ID to update: "))
        new_title = input("Enter new title: ")
        new_author = input("Enter new author: ")
        new_total = int(input("Enter new total copies: "))

        cursor = conn.cursor()
        query = """UPDATE books 
                   SET title=%s, author=%s, total_copies=%s, available_copies=%s
                   WHERE book_id=%s"""
        values = (new_title, new_author, new_total, new_total, book_id)
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Book updated successfully!")
        else:
            print("⚠️ No book found with that ID.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def delete_book():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        book_id = int(input("Enter Book ID to delete: "))
        cursor = conn.cursor()
        query = "DELETE FROM books WHERE book_id=%s"
        cursor.execute(query, (book_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Book deleted successfully!")
        else:
            print("⚠️ No book found with that ID.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def search_books():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        keyword = input("Enter title or author keyword to search: ")
        cursor = conn.cursor()
        query = """SELECT * FROM books 
                   WHERE title LIKE %s OR author LIKE %s"""
        like_pattern = f"%{keyword}%"
        cursor.execute(query, (like_pattern, like_pattern))
        rows = cursor.fetchall()
        if not rows:
            print("📭 No books found matching your search.")
            return
        print("\n🔍 Search Results:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, "
                  f"Total: {row[3]}, Available: {row[4]}")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def books_menu():
    while True:
        print("\n====== 📚 Book Management ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_books()
        elif choice == "6":
            break
        else:
            print("⚠️ Invalid choice, please try again.")

"logic for issuing and returning books"
from db_config import get_connection


def issue_book():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        cursor = conn.cursor()

        # Check if book is available
        cursor.execute("SELECT available_copies FROM books WHERE book_id=%s", (book_id,))
        book = cursor.fetchone()

        if not book:
            print("⚠️ Book not found.")
            return
        if book[0] <= 0:
            print("⚠️ No copies available.")
            return

        # Issue book (insert transaction)
        cursor.execute(
            "INSERT INTO transactions (book_id, member_id, issue_date) VALUES (%s, %s, CURDATE())",
            (book_id, member_id),
        )

        # Decrease available copies
        cursor.execute(
            "UPDATE books SET available_copies = available_copies - 1 WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()
        print("✅ Book issued successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def return_book():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        transaction_id = int(input("Enter Transaction ID to return book: "))
        cursor = conn.cursor()

        # Find transaction & book
        cursor.execute(
            "SELECT book_id, return_date FROM transactions WHERE transaction_id=%s",
            (transaction_id,)
        )
        trans = cursor.fetchone()

        if not trans:
            print("⚠️ Transaction not found.")
            return
        if trans[1] is not None:
            print("⚠️ Book already returned.")
            return

        book_id = trans[0]

        # Update transaction with return date
        cursor.execute(
            "UPDATE transactions SET return_date = CURDATE() WHERE transaction_id=%s",
            (transaction_id,)
        )

        # Increase available copies
        cursor.execute(
            "UPDATE books SET available_copies = available_copies + 1 WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()
        print("✅ Book returned successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def view_transactions():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT t.transaction_id, m.name, b.title, t.issue_date, t.return_date
            FROM transactions t
            JOIN members m ON t.member_id = m.member_id
            JOIN books b ON t.book_id = b.book_id
            ORDER BY t.transaction_id DESC
        """)
        rows = cursor.fetchall()

        if not rows:
            print("\n📭 No transactions yet.")
            return

        print("\n📜 All Transactions:")
        for row in rows:
            print(f"Txn ID: {row[0]}, Member: {row[1]}, Book: {row[2]}, "
                  f"Issue Date: {row[3]}, Return Date: {row[4]}")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def transactions_menu():
    while True:
        print("\n====== 🔄 Issue & Return Management ======")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View All Transactions")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            break
        else:
            print("⚠️ Invalid choice, please try again.")

"logic for managing members"

from db_config import get_connection


def add_member():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        name = input("Enter member name: ")
        email = input("Enter member email: ")

        cursor = conn.cursor()
        query = """INSERT INTO members (name, email, join_date) 
                   VALUES (%s, %s, CURDATE())"""
        values = (name, email)
        cursor.execute(query, values)
        conn.commit()
        print("✅ Member added successfully!")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def view_members():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()
        if not rows:
            print("\n📭 No members found in the library.")
            return
        print("\n👥 All Members:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Join Date: {row[3]}")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def update_member():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        member_id = int(input("Enter Member ID to update: "))
        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")

        cursor = conn.cursor()
        query = """UPDATE members 
                   SET name=%s, email=%s 
                   WHERE member_id=%s"""
        values = (new_name, new_email, member_id)
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Member updated successfully!")
        else:
            print("⚠️ No member found with that ID.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def delete_member():
    conn = get_connection()
    if conn is None:
        print("❌ Database connection failed.")
        return

    try:
        member_id = int(input("Enter Member ID to delete: "))
        cursor = conn.cursor()
        query = "DELETE FROM members WHERE member_id=%s"
        cursor.execute(query, (member_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Member deleted successfully!")
        else:
            print("⚠️ No member found with that ID.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def members_menu():
    while True:
        print("\n====== 👥 Member Management ======")
        print("1. Add Member")
        print("2. View All Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            update_member()
        elif choice == "4":
            delete_member()
        elif choice == "5":
            break
        else:
            print("⚠️ Invalid choice, please try again.")

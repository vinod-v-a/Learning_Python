"main menu and app runner"
from books import books_menu
from members import members_menu
from issue_return import transactions_menu

def main_menu():
    while True:
        print("\n========== 📖 Library Management System ==========")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Issue/Return Books")
        print("4. Exit")
        print("===============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            books_menu()
        elif choice == "2":
            members_menu()
        elif choice == "3":
            transactions_menu()
        elif choice == "4":
            print("👋 Exiting Library Management System. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()



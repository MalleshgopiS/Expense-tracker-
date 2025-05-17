from datetime import *
from transaction_report import *
from data_initialize import *


# Main CLI loop
def main():
    initialize_data()
    while True:
        print("\n--- Income & Expense Tracker ---")
        print("1. Add Transaction")
        print("2. View Transaction History")
        print("3. View Financial Report")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_history()
        elif choice == '3':
            show_report()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()




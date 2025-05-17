# Expense-tracker-

This Python program is an Income & Expense Tracker, designed to manage financial transactions by storing them in a JSON file. Here's a breakdown of how it works:

Key Features:
- Transaction Management
- Users can add transactions labeled as either income or expense.
- Transactions are categorized into Food, Freelance, or Other.
- Each entry includes the amount, a note, and a timestamp.
- Data Handling
- Transactions are stored in a JSON file (transactions.json).
- Functions ensure the file exists and properly loads the stored data.
- Transactions are safely written back to the file.
- Viewing & Reporting
- Users can view transaction history, displaying all records in a structured format.
- A financial report shows total income, total expenses, net balance, and expense breakdown by category.
- Command-Line Interface (CLI)
- A menu-driven approach allows users to interact easily.
- Options include adding transactions, viewing history, generating reports, and exiting.

Fixed Issues:
- Ensured transactions load as a list to prevent errors.
- Used proper list concatenation instead of append to add new transactions.
This tracker helps users monitor their finances effortlessly! 🚀 Let me know if you need enhancements or more details.


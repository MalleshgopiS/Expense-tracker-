import json
import os
from datetime import datetime

DATA_FILE = 'transactions.json'

# Initialize data file if not present
def initialize_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

# Load transactions from file
def load_transactions():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)  # Fix: Returns the loaded data

# Save transactions to file
def save_transactions(transactions):
    with open(DATA_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)

# Add a transaction (income or expense)
def add_transaction():
    print("\nAdd Transaction")
    trans_type = input("Type (income/expense): ").strip().lower()
    if trans_type not in ['income', 'expense']:
        print("Invalid type! Please enter 'income' or 'expense'.")
        return

    category = input("Category (Food / Freelance / Other): ").strip().capitalize()
    if category not in ['Food', 'Freelance', 'Other']:
        print("Invalid category! Defaulting to 'Other'.")
        category = 'Other'

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    note = input("Note (optional): ").strip()

    transaction = {
        'type': trans_type,
        'category': category,
        'amount': amount,
        'note': note,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    transactions = load_transactions()
    if not isinstance(transactions, list):  
        transactions = []  # Ensure transactions is always a list
    
    transactions = transactions + [transaction]  # Safe concatenation
    save_transactions(transactions)
    print("Transaction added successfully!")


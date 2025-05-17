from data_initialize import *

# Show all transaction history
def show_history():
    print("\nTransaction History")
    transactions = load_transactions()
    if not transactions:
        print("No transactions found.")
        return

    for t in transactions:
        print(f"{t['date']} | {t['type'].capitalize()} | {t['category']} | ₹ {t['amount']} | {t['note']}")

# Show financial report
def show_report():
    transactions = load_transactions()
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')

    print("\nFinancial Report")
    print(f"Total Income: ₹ {income}")
    print(f"Total Expense: ₹ {expense}")
    print(f"Net Balance: ₹ {income - expense}\n")

    print("Expenses by Category:")
    categories = {'Food': 0, 'Freelance': 0, 'Other': 0}
    for t in transactions:
        if t['type'] == 'expense':
            categories[t['category']] += t['amount']

    for cat, amt in categories.items():
        print(f"  {cat}: ₹ {amt}")
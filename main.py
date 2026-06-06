import json

FILE_NAME = "expenses.json"

def load_expenses():
    with open( FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent =4) 


def add_expenses(expenses):
    description = input("description: ")
    try:
        amount = float(input("amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    category = input("category: ")

    expenses.append({"description": description,
        "amount": amount, "category": category})
    
    save_expenses(expenses)
    print("Expense Added!")

def view_expenses(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    print("\n === Expenses ===")
    
    for i, expense in enumerate(expenses, start=1):
        category = expense.get("category", "No Category")

        print(
            f"{i}. {expense['description']} "
            f"({category}) - "
            f"${expense['amount']:.2f}")

def view_total(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ${total:.2f}")

def delete_expenses(expenses):
    if not expenses:
        print("no expense to delete")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("Enter expense number to delete: "))
        index = index -1
    except ValueError:
        print("invalid input")
        return
    
    if  0 <= index < len(expenses):
        removed = expenses.pop(index)

        save_expenses(expenses)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")

def main():
    expenses = load_expenses()
    while True:
        print("\n===Expense Tracker===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Total")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            delete_expenses(expenses)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("invalid choice, try again")

main()
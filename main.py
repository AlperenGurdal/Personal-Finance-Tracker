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

def view_by_category(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    category_totals = {}
    total_spent = 0

    for expense in expenses:
        category = expense.get("category","No Category")
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        total_spent += amount


    print("\n=== Spending by Category ===")

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")  
    
    print("\n----------------------")
    print(f"TOTAL: ${total_spent:.2f}")

def edit_expenses(expenses):
    if not expenses:
        print("no expenses to edit")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("Enter Expense number to edit: "))-1
    except ValueError:
        print("invalid input")
        return
    
    expense = expenses[index]
    print("\nLeave blank to keep current value.")

    description = input(f"Description [{expense['description']}]: ")
    amount_input = input(f"Amount [{expense['amount']}]: ")
    category = input(f"description[{expense['category']}]: ")

    if description:
        expense["description"] = description

    if amount_input:
        try:
            expense["amount"] = float(amount_input)
        except ValueError:
            print("Invalid amount.")
            return

    if category:
        expense["category"] = category
    
    save_expenses(expenses)
    print("Expense updated!")


    
def main():
    expenses = load_expenses()
    while True:
        print("\n===Expense Tracker===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Total")
        print("4. View Expenses By Category")
        print("5. Edit Expense")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            view_by_category(expenses)
        elif choice == "5":
            edit_expenses(expenses)
        elif choice == "6":
            delete_expenses(expenses)
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("invalid choice, try again")

main()
import json

File_name = "expenses.json"

def load_expenses():
    with open( File_name, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(File_name, "w") as file:
        json.dump(expenses, file, indent =4) 


def add_expenses(expenses):
    description = input("description: ")
    amount = float(input("amount: "))

    expenses.append({"description": description,
        "amount": amount})
    
    save_expenses(expenses)
    print("Expense Added!")



def main():
    expenses = load_expenses()
    add_expenses(expenses)

main()
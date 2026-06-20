import tkinter as tk
from storage import load_expenses, save_expenses
from storage import (
    load_expenses,
    save_expenses,
    load_income,
    save_income
)

window = tk.Tk()
window.title("Finance Tracker")
window.geometry("600x600")

title_label = tk.Label(
    window,
    text="Finance Tracker",
    font=("Arial", 20)
)

title_label.pack(pady=20)

description_label = tk.Label(window, text="Description")
description_label.pack()

description_entry = tk.Entry(window)
description_entry.pack()

amount_label = tk.Label(window, text="Amount")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

category_label = tk.Label(window, text="Category")
category_label.pack()

category_entry = tk.Entry(window)
category_entry.pack()

def add_expense():
    description = description_entry.get()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        print("Invalid amount")
        return

    category = category_entry.get()

    expenses = load_expenses()

    expenses.append({
        "description": description,
        "amount": amount,
        "category": category
    })

    save_expenses(expenses)

    refresh_expenses()

add_button = tk.Button(
    window,
    text="Add Expense",
    command=add_expense
)

add_button.pack(pady=10) 

expense_listbox = tk.Listbox(window, width=60)
expense_listbox.pack(pady=10)

def refresh_expenses():
    expense_listbox.delete(0, tk.END)

    expenses = load_expenses()

    total = 0

    for expense in expenses:
        expense_listbox.insert(
            tk.END,
            f"{expense['description']} ({expense['category']}) - ${expense['amount']:.2f}"
        )
        total += expense["amount"]
    
    total_label.config(text=f"Total Spent: ${total:.2f}")

def delete_expense():
    selected = expense_listbox.curselection()

    if not selected:
        print("No expense selected")
        return

    index = selected[0]

    expenses = load_expenses()

    expenses.pop(index)

    save_expenses(expenses)

    refresh_expenses()

delete_button = tk.Button(
    window,
    text="Delete Selected",
    command=delete_expense
)

def edit_expense():
    selected = expense_listbox.curselection()

    if not selected:
        print("No expense selected")
        return

    index = selected[0]

    expenses = load_expenses()

    expenses[index]["description"] = description_entry.get()

    try:
        expenses[index]["amount"] = float(amount_entry.get())
    except ValueError:
        print("Invalid amount")
        return

    expenses[index]["category"] = category_entry.get()

    save_expenses(expenses)

    refresh_expenses()

edit_button = tk.Button(
    window,
    text="Edit Selected",
    command=edit_expense
)

edit_button.pack(pady=5)

delete_button.pack(pady=5)

total_label = tk.Label(window, text="Total Spent: $0.00")
total_label.pack(pady=5)

def load_selected(event):
    selected = expense_listbox.curselection()

    if not selected:
        return

    index = selected[0]

    expenses = load_expenses()

    expense = expenses[index]

    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    description_entry.insert(0, expense["description"])
    amount_entry.insert(0, str(expense["amount"]))
    category_entry.insert(0, expense["category"])

expense_listbox.bind("<<ListboxSelect>>", load_selected)


refresh_expenses()
window.mainloop()
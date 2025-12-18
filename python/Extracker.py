
import tkinter as tk

class ExpenseTracker:
    def __init__(self):
        self.date = ""
        self.amount = 0
        self.category = ""
        self.description = ""

    def addexpense(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def viewexpense(self):
        return f"Date: {self.date}\nAmount: {self.amount}\nCategory: {self.category}\nDescription: {self.description}"

    def deleteexpense(self):
        self.date = ""
        self.amount = 0
        self.category = ""
        self.description = ""

tracker = ExpenseTracker()

def add_expense():
    tracker.addexpense(
        date_entry.get(),
        float(amount_entry.get()),
        category_entry.get(),
        description_entry.get()
    )
    result_label.config(text="Expense Added!")

def view_expense():
    result_label.config(text=tracker.viewexpense())

def delete_expense():
    tracker.deleteexpense()
    result_label.config(text="Expense Deleted!")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Date:").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1)

tk.Label(root, text="Description:").grid(row=3, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=7, column=0)
tk.Button(root, text="View Expense", command=view_expense).grid(row=7, column=1)
tk.Button(root, text="Delete Expense", command=delete_expense).grid(row=7, column=2)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=3)

root.mainloop()

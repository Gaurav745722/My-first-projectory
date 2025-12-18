import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if name and email and password:
        messagebox.showinfo("Success", f"Registered Successfully!\nName: {name}\nEmail: {email}")
    else:
        messagebox.showwarning("Error", "Please fill all fields!")

# Create main window
root = tk.Tk()
root.title("Simple Registration Form")
root.geometry("300x200")

# Labels & Entry fields
tk.Label(root, text="Name").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Password").grid(row=2, column=0, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1)

# Submit button
tk.Button(root, text="Submit", command=submit).grid(row=3, column=1, pady=10)

root.mainloop()

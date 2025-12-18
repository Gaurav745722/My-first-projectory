import csv
from datetime import datetime
import os

FILE_NAME = 'expenses.csv'

# Create file with headers if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Description', 'Amount'])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Transport, Rent): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully.\n")

def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print(f"{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>10}")
        print("-" * 60)
        for row in reader:
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<20} ₹{float(row[3]):>8.2f}")

def total_spent():
    total = 0.0
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[3])
    print(f"\nTotal Spent: ₹{total:.2f}\n")

def filter_expenses():
    choice = input("Filter by (1) Date or (2) Category? Enter 1 or 2: ")
    keyword = input("Enter date (YYYY-MM-DD) or category: ")
    
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        found = False
        print(f"\n{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':>10}")
        print("-" * 60)
        for row in reader:
            if keyword.lower() in row[int(choice)-1].lower():
                print(f"{row[0]:<12} {row[1]:<15} {row[2]:<20} ₹{float(row[3]):>8.2f}")
                found = True
        if not found:
            print("No matching records found.")

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Show Total Spent")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_expenses()
        elif choice == '4':
            total_spent()
        elif choice == '5':
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()

import csv
from datetime import datetime
FILE_NAME = "expenses.csv"
def create_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Type", "Amount"])
    except FileExistsError:
        pass
def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    entry_type = input("Income or Expense: ").capitalize()
    amount = float(input("Enter amount: "))
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, entry_type, amount])
    print("Entry added successfully!")
def view_entries():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    income = 0
    expense = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                amount = float(row["Amount"])
                if row["Type"] == "Income":
                    income += amount
                elif row["Type"] == "Expense":
                    expense += amount
    print("\nMonthly Summary")
    print("----------------")
    print("Income :", income)
    print("Expense:", expense)
    print("Balance:", income - expense)
def main():
    create_file()
    while True:
        print("\nExpense Tracker CLI")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
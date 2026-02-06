from datetime import datetime

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = datetime.now().strftime("%d-%m-%Y")

    with open("expense.txt", "a") as file:
        file.write(f"{date} | {category} | {amount}\n")

    print("Expense added!\n")


def view_expense():
    try:
        with open("expense.txt", "r") as file:
            print("\n--- Expense List ---")
            print(file.read())
    except FileNotFoundError:
        print("No expenses found.\n")


def total_expense():
    total = 0
    try:
        with open("expense.txt", "r") as file:
            for line in file:
                amount = line.split("|")[2]
                total += float(amount)
        print("Total Expense:", total)
    except FileNotFoundError:
        print("No expenses found.\n")


def delete_all_expenses():
    open("expense.txt", "w").close()
    print("All expenses deleted!\n")


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete All Expenses")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        delete_all_expenses()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice\n")

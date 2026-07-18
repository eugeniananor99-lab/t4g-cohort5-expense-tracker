"""expenses = []
print ("expense")


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. view Expense")
    print("3. show Total")
    print("4. Exiit")
    
    choice = input("choose an option")

    if choice == "1":
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))
        expense = {
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(f"Description: {expense['description']}, Amount: {expense['amount']}")


                
    elif choice == "3":
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: {total}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")"""



                 
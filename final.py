# Simple Expense Tracker

expenses = []

print("===== EXPENSE TRACKER =====")

salary = float(input("Enter your monthly salary: ₹"))
yearly_salary = salary * 12

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Yearly Spending and Savings")
    print("4. View Monthly Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Expense
    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter expense amount: ₹"))

        expenses.append({
            "date": date,
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    # View All Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            for expense in expenses:
                print(
                    expense["date"],
                    expense["category"],
                    "₹", expense["amount"]
                )

    # Yearly Spending and Savings
    elif choice == "3":
        year = input("Enter year (YYYY): ")

        total = 0

        for expense in expenses:
            if expense["date"][:4] == year:
                total = total + expense["amount"]

        print("\n===== YEARLY REPORT =====")
        print("Year:", year)
        print("Yearly Salary: ₹", yearly_salary)
        print("Total Yearly Expenses: ₹", total)
        print("Yearly Savings: ₹", yearly_salary - total)

        if total > yearly_salary:
            print("Warning: You spent more than your yearly salary!")

    # Monthly Statistics
    elif choice == "4":
        monthly_total = {}

        for expense in expenses:
            month = expense["date"][:7]

            if month not in monthly_total:
                monthly_total[month] = 0

            monthly_total[month] += expense["amount"]

        if len(monthly_total) == 0:
            print("No monthly data available.")
        else:
            for month in monthly_total:
                print(
                    month,
                    "Spending: ₹",
                    monthly_total[month]
                )

            # Average Monthly Spending
            total_spending = sum(monthly_total.values())
            average = total_spending / len(monthly_total)

            print(
                "Average Monthly Spending: ₹",
                round(average, 2)
            )

            # Highest and Lowest Spending Months
            highest_month = max(
                monthly_total,
                key=monthly_total.get
            )

            lowest_month = min(
                monthly_total,
                key=monthly_total.get
            )

            print("Highest Spending Month:", highest_month)
            print("Lowest Spending Month:", lowest_month)

    # Exit
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
print("======WEEKLY EXPENSES CALCULATOR=======")

daily_expenses = int(input("Enter your daily expense in naira: "))
if daily_expenses < 0:
    print("Error: Expense cannot be negative.")
days = int(input("Enter the number of days: "))
if days < 0:
    print("Error: Number of days cannot be negative.")


total_expenses = daily_expenses * days
budget = int(input("Enter your weekly budget in naira: "))

if budget < 0:
    print("Error: Budget cannot be negative")


if total_expenses < budget:
    remaining = budget - total_expenses
    print("Status: Within budget")
    print(f"Amount remaining: NGN {remaining}")

elif total_expenses == budget:
    print("Status: Exactly on budget")
    print("Amount remaining: NGN 0")

else:
    exceeded = total_expenses - budget
    print("Status: Over budget")
    print(f"Amount exceeded: NGN {exceeded}")
    

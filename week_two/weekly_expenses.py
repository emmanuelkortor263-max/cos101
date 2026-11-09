#Enter student information
student_name = input("Enter student name: ")
daily_transport_cost = float(input("Enter daily transport cost (£): "))
daily_feeding_cost = float(input("Enter daily feeding cost (£): "))
days = int(input("Enter number of days on campus: "))
other_expenses = float(input("Enter other expenses for the week (£): "))

#Calculate totals
transport_total = daily_transport_cost * days
feeding_total = daily_feeding_cost * days
weekly_total = transport_total + feeding_cost + other_expenses

print(transport_total)
print(feeding_total)
print(weekly_total)

# This is a program that ask for student information and feeding

#input
student_name = str(input("Enter student name:"))
daily_transport = int(input("Daily transport cost:"))
daily_feeding = int(input("Daily feeding cost:"))
number_of_days = int(input("Days in campus:"))
other_expenses = int(input("other fees:"))

#process
transportation_fees = daily_transport*number_of_days
feeding_fees =daily_feeding * number_of_days
total_expenses = transportation_fees+feeding_fees+other_expenses

#output
print ()
print ("//////////WEEKLY EXPENSES/////////")
print ()
print (f"student name:{student_name}")
print (f"Transport total:NGN {transportation_fees}")
print (f"feeding total:NGN {feeding_fees}")
print (f"other expenses:NGN {other_expenses}")
print (f"Weekly Total:NGN {total_expenses}")
       

student_name = str(input("Enter the student name:" ))
score = float(input("Enter student score:" ))

if score < 0 or score > 100:
    print("Invalid score. score must be between 0 and 100.")
else:
    if score >= 70:
        grade="A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
        


print("STUDENT RESULT")
print("====================")
print(f"Name: {student_name}")
print(f"score: {score}")
print(f"grade: {grade}")

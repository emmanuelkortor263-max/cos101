score = float(input("Enter Your Score"))

if score < 0 or score > 100:
    print("invalid score")
elif score >= 50:
    print("You pass")
else:
    print("You failed")

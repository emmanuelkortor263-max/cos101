#this programme displays the multiplication of numbers greater than one
while True:
    try:
        user = input("enter a number greater than 1: ")
        if user.lower() == "e":
            print("leave")
            break
        
        number = int(user)

        if number < 1:
            print("the number must be greater than 1")
            continue
#display of multiplication table
        print(f"\n---multi table for {number}---")
        for i in range(1,13):
            print(f"{number} x {i} = {number*i}")
        print("-" * 35)

    except ValueError:
        print("error")

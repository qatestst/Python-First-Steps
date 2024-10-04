age = float(input())
gender = input()

if gender.lower() == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender.lower() == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
else:
    print("Error")

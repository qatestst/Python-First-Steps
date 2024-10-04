day_of_week = int(input("Enter a number: "))

if 1 <= day_of_week <= 7:
    if day_of_week == 1:
        print("Monday")
    elif day_of_week == 2:
        print("Tuesday")
    elif day_of_week == 3:
        print("Wednesday")
    elif day_of_week == 4:
        print("Thursday")
    elif day_of_week == 5:
        print("Friday")
    elif day_of_week == 6:
        print("Saturday")
    elif day_of_week == 7:
        print("Sunday")
else:
    print("Error")

# Other solution using an Array
# day_of_week = int(input("Enter a number: "))
#
# if 1 <= day_of_week <= 7:
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     print(days[day_of_week - 1])
# else:
#     print("Error")

# days = {
#     "Monday": 12,
#     "Tuesday": 12,
#     "Wednesday": 14,
#     "Thursday": 14,
#     "Friday": 12,
#     "Saturday": 16,
#     "Sunday": 16
# }
#
# day_of_week = input("Enter day of the week: ")
#
# if day_of_week in days:
#     print(days[day_of_week])
# else:
#     print("Error")

day = input()
price = 0
if day == "Monday" or day == "Tuesday" or day == "Friday":
    price = 12
    print(price)
elif day == "Wednesday" or day == "Thursday":
    price = 14
    print(price)
elif day == "Saturday" or day == "Sunday":
    price = 16
    print(price)


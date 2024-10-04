day_of_week = input()

if (day_of_week.lower() == "monday" or
        day_of_week.lower() == "tuesday" or
        day_of_week.lower() == "wednesday" or
        day_of_week.lower() == "thursday" or
        day_of_week.lower() == "friday"):
    print("Working day")
elif day_of_week.lower() == "saturday" or day_of_week.lower() == "sunday":
    print("Weekend")
else:
    print("Error")

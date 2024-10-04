# Read input from the user
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Convert exam and arrival times to minutes
exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

# Calculate the difference in minutes
time_difference = arrival_time - exam_time

# Determine the student's status
if time_difference > 0:
    print("Late")
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif -30 <= time_difference <= 0:
    print("On time")
    if time_difference != 0:
        print(f"{abs(time_difference)} minutes before the start")
else:
    print("Early")
    if abs(time_difference) < 60:
        print(f"{abs(time_difference)} minutes before the start")
    else:
        hours = abs(time_difference) // 60
        minutes = abs(time_difference) % 60
        print(f"{hours}:{minutes:02d} hours before the start")

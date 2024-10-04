import math

serie_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4

total_break_time = lunch_time + rest_time
remaining_time = break_length - total_break_time

if remaining_time >= episode_length:
    print(f"You have enough time to watch {serie_name} and left with {int(math.ceil(remaining_time - episode_length))} minutes free time.")
else:
    print(f"You don't have enough time to watch {serie_name}, you need {int(math.ceil(episode_length - remaining_time))} more minutes.")

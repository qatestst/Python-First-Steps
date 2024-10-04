number = int(input())
bonus_points = 0
additional_bonus = 0

if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = 0.2 * number
elif number > 1000:
    bonus_points = 0.1 * number

if number % 2 == 0:
    additional_bonus = 1
elif number % 10 == 5:
    additional_bonus = 2

total_bonus_points = bonus_points + additional_bonus

print(total_bonus_points)
print(total_bonus_points + number)

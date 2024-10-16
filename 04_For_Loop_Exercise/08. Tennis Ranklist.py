# Входни данни
number_of_tournaments = int(input())
initial_points = int(input())

# Константи за точки
points_for_W = 2000
points_for_F = 1200
points_for_SF = 720

# Променливи за сума на точки и брой спечелени турнири
total_points = initial_points
total_wins = 0
total_points_earned = 0

# Обхождане на всички турнири
for _ in range(number_of_tournaments):
    stage = input()
    if stage == "W":
        total_points += points_for_W
        total_wins += 1
        total_points_earned += points_for_W
    elif stage == "F":
        total_points += points_for_F
        total_points_earned += points_for_F
    elif stage == "SF":
        total_points += points_for_SF
        total_points_earned += points_for_SF

# Изчисляване на средните точки и процент спечелени турнири
average_points = total_points_earned // number_of_tournaments
win_percentage = (total_wins / number_of_tournaments) * 100

# Изход
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")
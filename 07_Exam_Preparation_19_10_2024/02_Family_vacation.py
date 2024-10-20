budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percent = float(input()) / 100

if nights > 7:
    price_per_night = price_per_night - (price_per_night * 0.05)

total_cost = (price_per_night * nights)
exepnses = additional_expenses_percent * budget
total_cost = total_cost + exepnses

if budget >= total_cost:
    print(f"Ivanovi will be left with {budget - total_cost:.2f} leva after vacation.")
else:
    print(f"{total_cost - budget} leva needed.")

# Входни данни
budget = float(input())  # Бюджет на филма
destination = input()    # Дестинация ("Dubai", "Sofia" или "London")
season = input()         # Сезон ("Summer" или "Winter")
days = int(input())      # Брой снимачни дни

# Определяне на базовата цена за един ден
price_per_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250

# Обща сума за снимачните дни
total_price = days * price_per_day

# Приложение на отстъпки/оскъпявания
if destination == "Dubai":
    total_price *= 0.7  # 30% отстъпка
elif destination == "Sofia":
    total_price *= 1.25  # 25% оскъпяване

# Проверка дали бюджетът е достатъчен
if total_price <= budget:
    money_left = budget - total_price
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"The director needs {money_needed:.2f} leva more!")

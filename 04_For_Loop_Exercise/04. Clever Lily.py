# Входни данни
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

# Инициализация на променливи
money_saved = 0
toys_count = 0
money_received = 0

# Обхождане на годините
for year in range(1, age + 1):
    if year % 2 == 0:
        money_received += 10
        money_saved += money_received - 1  # Братът взима 1 лев
    else:
        toys_count += 1

# Добавяне на парите от продадените играчки
money_saved += toys_count * toy_price

# Проверка дали парите са достатъчни
if money_saved >= washing_machine_price:
    print(f"Yes! {money_saved - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money_saved:.2f}")

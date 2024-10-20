# Входни данни
price_strawberries = float(input())  # Цена на ягодите
quantity_bananas = float(input())    # Количество на бананите
quantity_oranges = float(input())    # Количество на портокалите
quantity_raspberries = float(input()) # Количество на малините
quantity_strawberries = float(input()) # Количество на ягодите

# Изчисляване на цените на плодовете
price_raspberries = price_strawberries / 2
price_oranges = price_raspberries * 0.6
price_bananas = price_raspberries * 0.2

# Изчисляване на общата сума
total_raspberries = quantity_raspberries * price_raspberries
total_oranges = quantity_oranges * price_oranges
total_bananas = quantity_bananas * price_bananas
total_strawberries = quantity_strawberries * price_strawberries

# Обща сума за всички плодове
total_price = total_raspberries + total_oranges + total_bananas + total_strawberries

# Форматиране и отпечатване на резултата
print(f"{total_price:.2f}")

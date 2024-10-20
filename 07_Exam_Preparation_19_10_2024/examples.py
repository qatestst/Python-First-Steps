# Въвеждаме цените и количествата на фруктовете, които Мария трябва да купи

price_strawberries = float(input())
banana_count = float(input())
orange_count = float(input())
raspberry_count = float(input())
strawberry_count = float(input())

# Обазначаваме цените и количествата на фруктовете в лева и килограми, съответно

price_malinas = price_strawberries / 2
discount_raspberry = int((40/100) * price_malinas)
price_raspberry = price_malinas - discount_raspberry
discount_banana = int((80/100) * price_malinas)
price_banana = price_malinas - discount_banana

# Сумаризираме цените и количествата на фруктовете в лева и килограми, съответно

strawberry_price = strawberry_count * price_strawberries
raspberry_price = raspberry_count * price_raspberry
orange_price = orange_count * (price_malinas - discount_raspberry)
banana_price = banana_count * price_banana

# Редица и печатаме сумата, която е необходима на Мария да плати сметката

total_price = round(strawberry_price + raspberry_price + orange_price + banana_price, 2)

print(total_price)
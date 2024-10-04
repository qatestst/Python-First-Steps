coffee_Sofia = 0.50
coffee_Plovdiv = 0.40
coffee_Varna = 0.45

water_Sofia = 0.80
water_Plovdiv = 0.70
water_Varna = 0.70

beer_Sofia = 1.20
beer_Plovdiv = 1.15
beer_Varna = 1.10

sweets_Sofia = 1.45
sweets_Plovdiv = 1.30
sweets_Varna = 1.35

peanuts_Sofia = 1.60
peanuts_Plovdiv = 1.50
peanuts_Varna = 1.55

product = input("Enter product: ")
city = input("Enter city: ")
quantity = float(input("Enter quantity: "))

if product == "coffee":
    if city == "Sofia":
        price = coffee_Sofia * quantity
    elif city == "Plovdiv":
        price = coffee_Plovdiv * quantity
    elif city == "Varna":
        price = coffee_Varna * quantity
elif product == "water":
    if city == "Sofia":
        price = water_Sofia * quantity
    elif city == "Plovdiv":
        price = water_Plovdiv * quantity
    elif city == "Varna":
        price = water_Varna * quantity
elif product == "beer":
    if city == "Sofia":
        price = beer_Sofia * quantity
    elif city == "Plovdiv":
        price = beer_Plovdiv * quantity
    elif city == "Varna":
        price = beer_Varna * quantity
elif product == "sweets":
    if city == "Sofia":
        price = sweets_Sofia * quantity
    elif city == "Plovdiv":
        price = sweets_Plovdiv * quantity
    elif city == "Varna":
        price = sweets_Varna * quantity
elif product == "peanuts":
    if city == "Sofia":
        price = peanuts_Sofia * quantity
    elif city == "Plovdiv":
        price = peanuts_Plovdiv * quantity
    elif city == "Varna":
        price = peanuts_Varna * quantity

print(price)

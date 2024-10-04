fruit = input()
day = input()
quantity = float(input())

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruit_list = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
fruit_price = 0

banana_price = 2.50
apple_price = 1.20
orange_price = 0.85
grapefruit_price = 1.45
kiwi_price = 2.70
pineapple_price = 5.50
grapes_price = 3.85


if day in weekend:
    banana_price = 2.70
    apple_price = 1.25
    orange_price = 0.90
    grapefruit_price = 1.60
    kiwi_price = 3.00
    pineapple_price = 5.60
    grapes_price = 4.20

if fruit == 'banana':
    fruit_price = banana_price
elif fruit == 'apple':
    fruit_price = apple_price
elif fruit == 'orange':
    fruit_price = orange_price
elif fruit == 'grapefruit':
    fruit_price = grapefruit_price
elif fruit == 'kiwi':
    fruit_price = kiwi_price
elif fruit == 'pineapple':
    fruit_price = pineapple_price
elif fruit == 'grapes':
    fruit_price = grapes_price


total_price = quantity * fruit_price

if day not in working_days and day not in weekend:
    print('error')
elif fruit not in fruit_list:
    print('error')
else:
    print(f'{total_price:.2f}')
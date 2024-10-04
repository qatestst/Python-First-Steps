from os import stat_result

PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

screening_type = input()
rows = int(input())
colums = int(input())

total_price = 0

all_seats = colums * rows

if screening_type == 'Premiere':
    total_price = all_seats * PREMIERE_PRICE
elif screening_type == 'Normal':
    total_price = all_seats * NORMAL_PRICE
elif screening_type == 'Discount':
    total_price = all_seats * DISCOUNT_PRICE

print(f'{total_price:.2f} leva')
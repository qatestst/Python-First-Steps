pens = int(input())
markers = int(input())
detergent_liters = int(input())
discount = float(input()) / 100  #percent discount

total_price = pens * 5.8 + markers * 7.20 + detergent_liters * 1.20
discount_sum = total_price * discount

needed_money = total_price - discount_sum

print(f'{needed_money:.2f}')

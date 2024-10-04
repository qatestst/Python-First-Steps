naylon = int(input()) + 2
paint = int(input())
razreditel = int(input())
hours = int(input())

total_sum = (naylon * 1.50) + ((paint * 14.50) * 1.1) + (razreditel * 5) + 0.40
price_for_painters_per_hour = total_sum * 0.3

final_price = hours * price_for_painters_per_hour + total_sum

print(f'{final_price:.2f}')




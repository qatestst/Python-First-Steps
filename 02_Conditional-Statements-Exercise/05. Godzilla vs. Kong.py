budget = float(input())
actors = int(input())
clothing_price_per_actor = float(input())

decor = 0.1 * budget

if actors > 150:
    clothing_price_per_actor = clothing_price_per_actor * 0.9

total_price = decor + (clothing_price_per_actor * actors)

if total_price <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with '
          f'{budget - total_price:.2f} leva left.')
elif total_price > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {total_price - budget:.2f} leva more.')

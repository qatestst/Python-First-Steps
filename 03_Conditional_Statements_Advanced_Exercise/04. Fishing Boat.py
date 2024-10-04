budget = float(input())
season = input()
fishermen = int(input())

# ship rent
ship_rent_spring = 3000
ship_rent_summer_and_autumn = 4200
ship_rent_winter = 2600

discount = 0

if fishermen <= 6 :
    discount = 0.10
elif 7 <= fishermen <= 11 :
    discount = 0.15
elif fishermen >= 12:
    discount = 0.25



total_cost = 0

if season == 'Spring':
    total_cost = ship_rent_spring - (discount * ship_rent_spring)
elif season == 'Summer' or season == 'Autumn':
    total_cost = ship_rent_summer_and_autumn - (discount * ship_rent_summer_and_autumn)
elif season == 'Winter':
    total_cost = ship_rent_winter - (discount * ship_rent_winter)

if fishermen % 2 == 0 and season != 'Autumn':
    total_cost = total_cost - (total_cost * 0.05)


if total_cost <= budget:
    print(f'Yes! You have {budget - total_cost:.2f} leva left.')
elif total_cost > budget:
    print(f'Not enough money! You need {total_cost - budget:.2f} leva.')


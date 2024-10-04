trip_price = float(input())

puzzles_count = int(input())
puppets_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles = puzzles_count * 2.6
puppets = puppets_count * 3
teddy_bears = teddy_bears_count * 4.10
minions = minions_count * 8.20
trucks = trucks_count * 2

all_toys_count = (puzzles_count + puppets_count + teddy_bears_count
                  + minions_count + trucks_count)

total_price = puzzles + puppets + teddy_bears + minions + trucks
if all_toys_count >= 50:
    total_price = total_price * 0.75

rent = 0.1 * total_price

final_money = total_price - rent

if final_money >= trip_price:
    print(f'Yes! {final_money - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - final_money:.2f} lv needed.')
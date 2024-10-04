annual_tax = float(input())
sneakers = annual_tax - annual_tax * 0.4
sport_suit = sneakers * 0.8
ball = 0.25 * sport_suit
accessories = 0.2 * ball

total_sum = annual_tax + sneakers + sport_suit + ball + accessories

print(f'{total_sum:.2f}')
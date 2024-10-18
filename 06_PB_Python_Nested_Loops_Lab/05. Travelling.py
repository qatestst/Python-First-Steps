destination = input()
while destination != 'End':
    min_budget = float(input())
    sum = 0.00  # Reset sum for each new destination
    while sum < min_budget:
            money = float(input())
            sum += money

    print(f"Going to {destination}!")
    destination = input()

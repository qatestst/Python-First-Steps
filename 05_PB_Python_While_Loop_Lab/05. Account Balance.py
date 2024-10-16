inpt = input()
balance = 0.0
while inpt != "NoMoreMoney":
    amount = float(inpt)
    if amount < 0:
        print(f"Invalid operation!")
        break
    elif amount > 0:
        balance += amount
        print(f'Increase: {amount:.2f}')
    inpt = input()
print(f"Total: {balance:.2f}")
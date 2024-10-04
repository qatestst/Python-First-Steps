city = input()
sales = float(input())

commission = 0.0

cities = ['Sofia', 'Varna', 'Plovdiv']

if city not in cities:
    print('error')
elif sales < 0:
    print('error')
elif city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    else:
        commission = sales * 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    else:
        commission = sales * 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    else:
        commission = sales * 0.145

if city in cities and sales >= 0:
    print(f'{commission:.2f}')

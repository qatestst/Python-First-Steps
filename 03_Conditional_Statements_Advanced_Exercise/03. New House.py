flowers_type = input()
count = int(input())
budget = float(input())

ROSES = 5
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

total_cost = 0

if flowers_type == 'Roses':
    if count > 80:
        ROSES *= 0.9
        total_cost = count * ROSES
    else:
        total_cost = count * ROSES

elif flowers_type == 'Dahlias':
    if count > 90:
        DAHLIAS *= 0.85
        total_cost = count * DAHLIAS
    else:
        total_cost = count * DAHLIAS
elif flowers_type == 'Tulips':
    if count > 80:
        TULIPS *= 0.85
        total_cost = count * TULIPS
    else:
        total_cost = count * TULIPS
elif flowers_type == 'Narcissus':
    if count < 120:
        NARCISSUS *= 1.15
        total_cost = count * NARCISSUS
    else:
        total_cost = count * NARCISSUS
elif flowers_type == 'Gladiolus':
    if count < 80:
        GLADIOLUS *= 1.2
        total_cost = count * GLADIOLUS
    else:
        total_cost = count * GLADIOLUS

if total_cost <= budget:
    print(f"Hey, you have a great garden with {count}"
          f" {flowers_type} and {budget - total_cost:.2f} leva left.")
else:
    print(f"Not enough money, you need "
          f"{total_cost - budget:.2f} leva more.")
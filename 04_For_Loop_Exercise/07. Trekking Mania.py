# Входни данни
num_groups = int(input())

# Инициализиране на броячи за всяка група
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

# Обхождане на всяка група
for _ in range(num_groups):
    group_size = int(input())
    total_climbers += group_size
    if group_size <= 5:
        musala += group_size
    elif group_size <= 12:
        monblan += group_size
    elif group_size <= 25:
        kilimanjaro += group_size
    elif group_size <= 40:
        k2 += group_size
    else:
        everest += group_size

# Изчисляване на процентите
musala_percent = (musala / total_climbers) * 100
monblan_percent = (monblan / total_climbers) * 100
kilimanjaro_percent = (kilimanjaro / total_climbers) * 100
k2_percent = (k2 / total_climbers) * 100
everest_percent = (everest / total_climbers) * 100

# Отпечатване на резултатите
print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

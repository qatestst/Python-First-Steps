# Прочитане на броя числа
n = int(input())

# Инициализация на броячи за всеки диапазон
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# Прочитане на числата и броене в съответните диапазони
for _ in range(n):
    num = int(input())
    if num < 200:
        count_p1 += 1
    elif 200 <= num < 400:
        count_p2 += 1
    elif 400 <= num < 600:
        count_p3 += 1
    elif 600 <= num < 800:
        count_p4 += 1
    else:
        count_p5 += 1

# Изчисляване на процентите
p1 = (count_p1 / n) * 100
p2 = (count_p2 / n) * 100
p3 = (count_p3 / n) * 100
p4 = (count_p4 / n) * 100
p5 = (count_p5 / n) * 100

# Отпечатване на резултатите с точност до две цифри след десетичната точка
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

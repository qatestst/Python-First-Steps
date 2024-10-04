# Четем броя на числата
n = int(input())

# Инициализираме сумите за четни и нечетни позиции
even_sum = 0
odd_sum = 0

# Четем числата и ги добавяме към съответната сума
for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

# Проверяваме дали сумите са равни и отпечатваме резултата
if even_sum == odd_sum:
    print("Yes")
    print("Sum =", even_sum)
else:
    print("No")
    print("Diff =", abs(even_sum - odd_sum))

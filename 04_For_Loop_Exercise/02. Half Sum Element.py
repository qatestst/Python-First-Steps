# Прочитане на броя числа
n = int(input())

# Инициализация на помощни променливи
max_num = float('-inf')
sum_numbers = 0

# Прочитане на числата и изчисляване на сумата и най-голямото число
for _ in range(n):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

# Проверка дали най-голямото число е равно на сумата на останалите
if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (sum_numbers - max_num))
    print("No")
    print(f"Diff = {diff}")

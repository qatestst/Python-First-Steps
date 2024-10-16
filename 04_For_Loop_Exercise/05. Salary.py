# Входни данни
n = int(input())
salary = int(input())

# Глоби за различните сайтове
penalties = {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50
}

# Обхождане на табовете
for _ in range(n):
    website = input()
    if website in penalties:
        salary -= penalties[website]
    if salary <= 0:
        print("You have lost your salary.")
        break

# Проверка на остатъка от заплатата
if salary > 0:
    print(f"{salary}")

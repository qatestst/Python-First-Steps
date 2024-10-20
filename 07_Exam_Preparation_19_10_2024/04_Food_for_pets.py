# Входни данни
days = int(input())  # Брой дни
total_food = float(input())  # Общо количество храна

# Инициализиране на променливи
total_dog_food = 0
total_cat_food = 0
total_biscuits = 0

# Обхождане на дните
for day in range(1, days + 1):
    dog_food = int(input())  # Храна, изядена от кучето
    cat_food = int(input())  # Храна, изядена от котката

    # Добавяме храната за деня
    total_dog_food += dog_food
    total_cat_food += cat_food

    # На всеки трети ден има бисквитки
    if day % 3 == 0:
        total_biscuits += 0.1 * (dog_food + cat_food)

# Обща изядена храна
total_eaten_food = total_dog_food + total_cat_food

# Пресмятане на процентите
percent_eaten_food = (total_eaten_food / total_food) * 100
percent_dog_food = (total_dog_food / total_eaten_food) * 100
percent_cat_food = (total_cat_food / total_eaten_food) * 100

# Закръгляне и форматиране на резултата
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")

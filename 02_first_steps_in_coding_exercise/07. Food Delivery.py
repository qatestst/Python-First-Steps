chicken = int(input()) * 10.35
fish = int(input()) * 12.40
vegetarian = int(input()) * 8.15

all_menus = chicken + fish + vegetarian

dessert = all_menus * 0.2

total_sum = 2.5 + all_menus + dessert

print(f'{total_sum:.2f}')
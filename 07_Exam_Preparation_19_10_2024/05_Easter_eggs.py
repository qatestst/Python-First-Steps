# Входни данни
eggs_player_one = int(input())  # Брой яйца на първия играч
eggs_player_two = int(input())  # Брой яйца на втория играч

# Започваме да четем командите
while True:
    command = input()  # Четем командата

    # Ако командата е "End", приключваме играта
    if command == "End":
        print(f"Player one has {eggs_player_one} eggs left.")
        print(f"Player two has {eggs_player_two} eggs left.")
        break

    # Ако първият играч печели
    if command == "one":
        eggs_player_two -= 1  # Вторият играч губи едно яйце
        if eggs_player_two == 0:  # Проверяваме дали вторият играч е останал без яйца
            print(f"Player two is out of eggs. Player one has {eggs_player_one} eggs left.")
            break

    # Ако вторият играч печели
    elif command == "two":
        eggs_player_one -= 1  # Първият играч губи едно яйце
        if eggs_player_one == 0:  # Проверяваме дали първият играч е останал без яйца
            print(f"Player one is out of eggs. Player two has {eggs_player_two} eggs left.")
            break

# Въвеждане на размерите на свободното пространство
width = int(input())
length = int(input())
height = int(input())

# Изчисляване на общия обем на свободното пространство
total_volume = width * length * height

# Докато има свободно пространство
while total_volume > 0:
    command = input()

    if command == "Done":
        print(f"{total_volume} Cubic meters left.")
        break

    boxes = int(command)
    total_volume -= boxes

    if total_volume < 0:
        print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
        break
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")

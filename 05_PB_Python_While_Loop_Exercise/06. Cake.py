# Въвеждане на размерите на тортата
width = int(input())
length = int(input())

# Изчисляване на общия брой парчета торта
total_pieces = width * length

# Докато има парчета торта
while total_pieces > 0:
    command = input()

    if command == "STOP":
        print(f"{total_pieces} pieces are left.")
        break

    taken_pieces = int(command)
    total_pieces -= taken_pieces

    if total_pieces < 0:
        print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
        break
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")

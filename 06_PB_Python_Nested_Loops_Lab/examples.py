#Example - Clock 24 hours
# for h in range(24):
#     for m in range(60):
#         print(f"{h}:{m}")

# Tablica za umnojenie
# for x in range(1, 11):
#   for y in range(1, 11):
#     product = x * y
#     print(f"{x} * {y} = {product}")

# # Example Magic number
# starting_number = int(input())
# final_number = int(input())
# magic_number = int(input())
# combinations = 0
# is_found = False
# for i in range(starting_number, final_number + 1):
#     for j in range(starting_number, final_number + 1):
#         combinations += 1
#         if i + j == magic_number:
#             print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
#             is_found = True
#             break
#     if is_found:
#         break
# if is_found is False:
#     print(f"There is no coincidence")

#Example - Building with rooms and apartments
floors = int(input())
rooms = int(input())

for i in range(floors,0,-1):
    for j in range (0,rooms):
        if i == floors:
            #print(f"L{i}{j} ", end="")
            print("L{0}{1} ".format(i,j),end = "")
        elif i % 2 == 0:
            print(f'O{i}{j} ', end = "")
        elif i % 2 != 0:
            print(f"A{i}{j} ", end = "")
    print("")
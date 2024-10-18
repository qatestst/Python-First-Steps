start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_counter = 0
is_found = False

for i in range(start_number, end_number+1):
    for y in range(start_number, end_number+1):
        combination_counter += 1
        if (i+y) == magic_number:
            print(f"Combination N:{combination_counter} ({i}"
                  f" + {y} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if is_found == False:
    print(f"{combination_counter} combinations -"
          f" neither equals {magic_number}")
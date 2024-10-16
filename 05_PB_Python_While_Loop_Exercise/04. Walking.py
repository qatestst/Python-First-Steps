goal = 10000
total_steps = 0

while total_steps < goal:
    command = input()

    if command == "Going home":
        steps = int(input())
        total_steps += steps
        break
    else:
        steps = int(command)
        total_steps += steps

if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
else:
    print(f"{goal - total_steps} more steps to reach goal.")

# Входни данни
actor_name = input()
initial_points = float(input())
n = int(input())

# Обхождане на оценяващите
for _ in range(n):
    judge_name = input()
    judge_points = float(input())
    initial_points += (len(judge_name) * judge_points) / 2
    if initial_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!")
        break
else:
    needed_points = 1250.5 - initial_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")

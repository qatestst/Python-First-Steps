bad_grades_limit = int(input())
bad_grades_counter = 0
tasks_counter = 0
grades_sum = 0

task_name = input()
last_task_name = ''

while task_name != 'Enough':
    grade = int(input())
    tasks_counter += 1
    last_task_name = task_name
    grades_sum += grade
    if grade <= 4.00:
        bad_grades_counter += 1
    if bad_grades_counter == bad_grades_limit:
        print(f"You need a break, {bad_grades_counter} poor grades.")
        break

    task_name = input()

if task_name == 'Enough':
    print(f"Average score: {grades_sum/tasks_counter:.2f}")
    print(f"Number of problems: {tasks_counter}")
    print(f"Last problem: {last_task_name}")



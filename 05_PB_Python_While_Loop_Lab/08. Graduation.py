name = input()
total_grades = 0
passed_years = 0
failed_years = 0
current_class = 1

while current_class <= 12:
    grade = float(input())
    if grade >= 4.00:
        total_grades += grade
        passed_years += 1
        current_class += 1
    else:
        failed_years += 1
        if failed_years > 1:
            print(f"{name} has been excluded at {current_class} grade")
            break
else:
    average_grade = total_grades / passed_years
    print(f"{name} graduated. Average grade: {average_grade:.2f}")


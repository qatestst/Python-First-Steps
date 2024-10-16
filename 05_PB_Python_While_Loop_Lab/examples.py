# Example 1
# a = 5
# while True:
#     if a > 10:
#         break
#     print("a = " + str(a))
#
import sys

# Example 2
# while True:
#     line = input()
#     if line == "Stop":
#         break
#     print("Loop")

# Example 3
# while True:
#   line = input()
#
#   if line == "Stop":
#     break
#
#   print(line)
#

# Example 4
# username = input()
# password = input()
#
# data = input()
# while data != password:
#     data = input()
# print(f"Welcome {username} !")

#Example 5
# n = int(input())
# sum = 0
#
# while sum < n:
#     current_num = int(input())
#     sum += current_num
# print(sum)

#Example 6
# inpt = input()
# balance = 0.0
# while inpt != "NoMoreMoney":
#     amount = float(inpt)
#     if amount < 0:
#         balance -= amount
#         print(f"Decrease: {amount:.2f}")
#     elif amount > 0:
#         balance += amount
#         print(f'Increase: {amount:.2f}')
#     inpt = input()
# print(f"Total: {balance:.2f}")

#Example 7
# number = input()
# max_number = -10000000000000
#
# while number != "Stop":
#     num = int(number)
#
#     if num > max_number:
#         max_number = num
#     number = input()
#
# print(max_number)

#Example 8
# number = input()
# min_number = sys.maxsize
# while number != 'Stop':
#     num = int(number)
#     if min_number > num:
#         min_number = num
#     number = input()
# print(min_number)

#Example 8 - Operator continue
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue # bypass the iteration and continue to next
#     print(i)
#     i += 1

# Example 9 - Graduation
# name = input()
# total_grades = 0
# passed_years = 0
# failed_years = 0
# current_class = 1
#
# while current_class <= 12:
#     grade = float(input())
#     if grade >= 4.00:
#         total_grades += grade
#         passed_years += 1
#         current_class += 1
#     else:
#         failed_years += 1
#         if failed_years > 1:
#             print(f"{name} has been excluded at {current_class} grade")
#             break
# else:
#     average_grade = total_grades / passed_years
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")
#





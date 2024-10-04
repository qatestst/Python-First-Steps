import sys

n = int(input())
smallest_number = sys.maxsize
largest_number = -sys.maxsize

for i in range(0,n):
    num = int(input())
    if num < smallest_number:
        smallest_number = num
    if num > largest_number:
        largest_number = num

print(f"Max number: {largest_number}")
print(f"Min number: {smallest_number}")
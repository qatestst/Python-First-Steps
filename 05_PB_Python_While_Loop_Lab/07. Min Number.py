import  sys
number = input()
min_number = sys.maxsize
while number != 'Stop':
    num = int(number)
    if min_number > num:
        min_number = num
    number = input()
print(min_number)
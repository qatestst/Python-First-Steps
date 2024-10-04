# Read input from the user
n = int(input())

# Print even powers of 2 up to 2^n
for i in range(0, n + 1, 2):
    print(2 ** i)

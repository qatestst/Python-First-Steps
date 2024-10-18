import sys

n = int(input())
combinations = 0

for i in range(0, n+1):
    for y in range(0,n+1):
        for z in range(0,n+1):
            if (i+y+z) == n:
                combinations += 1
print(combinations)
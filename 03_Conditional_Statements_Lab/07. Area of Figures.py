from math import pi,pow

figure_type = str(input())
area = 0

if figure_type == 'square':
    side_a = float(input())
    area = side_a * side_a
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == 'circle':
    radius = float(input())
    area = pi * pow(radius,2)
elif figure_type == 'triangle':
    side_a = float(input())
    height_to_side_a = float(input())
    area = 0.5 * side_a * height_to_side_a

print(f'{area:.2f}')

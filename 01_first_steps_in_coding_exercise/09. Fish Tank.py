length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_cm3 = length * width * height
volume_l = volume_cm3 / 1000.0

occupied_volume = volume_l * (percentage / 100.0)
water_volume = volume_l - occupied_volume

print(water_volume)

import math

world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())

delay = math.floor(distance_in_meters // 15)
total_delay = delay * 12.5

time = time_for_one_meter * distance_in_meters + total_delay

if time < world_record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
elif time >= world_record_in_seconds:
    print(f'No, he failed! He was {time - world_record_in_seconds:.2f} seconds slower.')

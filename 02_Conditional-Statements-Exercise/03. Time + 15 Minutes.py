hours = int(input())
minutes = int(input())

time_to_minutes = hours * 60 + minutes
total_minutes = time_to_minutes + 15

final_hours = total_minutes // 60
final_minutes = total_minutes % 60

if final_hours > 23:
    final_hours = 0

if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else:
    print(f'{final_hours}:{final_minutes}')

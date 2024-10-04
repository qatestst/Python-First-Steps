speed_input = float(input())

if speed_input <= 10:
    print('slow')
elif 10 < speed_input <=50:
    print('average')
elif 50 < speed_input <=150:
    print('fast')
elif 150 < speed_input <=1000:
    print('ultra fast')
elif speed_input > 1000:
    print('extremely fast')
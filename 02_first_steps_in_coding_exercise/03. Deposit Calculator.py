deposit = float(input())
months = int(input())
annual_interest_rate = float(input()) / 100



accumulated_interest = deposit * annual_interest_rate
interest_for_one_month = accumulated_interest / 12

final_sum = deposit + (months * interest_for_one_month)

print(f'{final_sum}')

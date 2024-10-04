budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = float(video_cards * 250)
processor_price = video_cards_price * 0.35 * processors
ram_memory_price = video_cards_price * 0.10 * ram_memory
total_cost = video_cards_price + processor_price + ram_memory_price

if video_cards > processors:
    total_cost *= 0.85

if total_cost <= budget:
    print(f"You have {budget - total_cost:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_cost - budget:.2f} leva more!")

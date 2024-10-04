# Read input from the user
days = int(input())
room_type = input()
rating = input()

# Calculate the number of nights
nights = days - 1

# Prices per night
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Calculate initial cost
initial_cost = price_per_night * nights

# Apply discounts based on the number of nights
if room_type == "apartment":
    if nights > 15:
        initial_cost *= 0.50
    elif 10 <= nights <= 15:
        initial_cost *= 0.65
    elif nights < 10:
        initial_cost *= 0.70
elif room_type == "president apartment":
    if nights > 15:
        initial_cost *= 0.80
    elif 10 <= nights <= 15:
        initial_cost *= 0.85
    elif nights < 10:
        initial_cost *= 0.90

# Apply rating adjustment
if rating == "positive":
    final_cost = initial_cost * 1.25
elif rating == "negative":
    final_cost = initial_cost * 0.90

# Print the final cost
print(f"{final_cost:.2f}")

# Read input from the user
month = input()
nights = int(input())

# Prices per night
studio_price = 0
apartment_price = 0

# Determine the prices based on the month
if month in ["May", "October"]:
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.70  # 30% discount
    elif nights > 7:
        studio_price *= 0.95  # 5% discount
elif month in ["June", "September"]:
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.80  # 20% discount
elif month in ["July", "August"]:
    studio_price = 76
    apartment_price = 77

# Apply discount for apartment if nights > 14
if nights > 14:
    apartment_price *= 0.90  # 10% discount

# Calculate total cost
total_studio = studio_price * nights
total_apartment = apartment_price * nights

# Print the results
print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")

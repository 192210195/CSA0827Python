# Input number of fresh and day-old loaves
fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day old loaves purchased: "))

# Regular price of fresh loaf
regular_price_fresh = fresh_loaves * 185

# Discounted price of day-old loaf (60% discount)
discounted_price_day_old = day_old_loaves * (185 * 0.4)  # 40% of original price

# Total price
total_price = regular_price_fresh + discounted_price_day_old

# Display the results
print(f"Regular price for fresh loaves: {regular_price_fresh:.2f} rupees")
print(f"Discount for day-old loaves: {discounted_price_day_old:.2f} rupees")
print(f"Total price: {total_price:.2f} rupees")

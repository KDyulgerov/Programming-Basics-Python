
area = float(input())

quality = float(7.61)

full_price = area * quality
discount_price = full_price * 0.18
discount_sum = full_price - discount_price

print(f"The final price is: {discount_sum} lv.")
print(f"The discount is: {discount_price} lv.")

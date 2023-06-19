
nylon_per_meter = 1.50
paint_per_liter = 14.50
liquid_per_liter = 5.00
bags = 0.40

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_liquid = int(input())
hours_for_work = int(input())

price_for_nylon = nylon_per_meter * (quantity_nylon + 2)
price_for_paint = paint_per_liter * (quantity_paint + (quantity_paint * 10 / 100))
price_for_liquid = liquid_per_liter * quantity_liquid

total_price = price_for_nylon + price_for_paint + price_for_liquid + bags
price_for_workers = (total_price * 30 / 100) * hours_for_work
final_price = total_price + price_for_workers

print(final_price)

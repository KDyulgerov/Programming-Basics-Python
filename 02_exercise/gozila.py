
budget = float(input())
count_actors = int(input())
price_clothes = float(input())

decor = budget * 10 / 100
clothes = price_clothes * count_actors

if count_actors > 150:
    clothes -= clothes * 10 / 100

total_price = clothes + decor

if total_price > budget:
    need_sum = abs(budget - total_price)
    print("Not enough money!")
    print(f"Wingard needs {need_sum:.2f} leva more.")

if total_price <= budget:
    sum_left = abs(budget - total_price)
    print("Action!")
    print(f"Wingard starts filming with {sum_left:.2f} leva left.")

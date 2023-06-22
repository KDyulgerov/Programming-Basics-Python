
vacation_price = float(input())
puzzle_count = int(input())
barbie_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
barbie_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_counts = puzzle_count + barbie_count + bears_count + minions_count + trucks_count
sum_puzzle = puzzle_count * puzzle_price
sum_barbie = barbie_count * barbie_price
sum_bear = bears_count * bear_price
sum_minion = minions_count * minion_price
sum_truck = trucks_count * truck_price

sum_total = sum_puzzle + sum_barbie + sum_bear + sum_minion + sum_truck

if total_counts >= 50:
    sum_total = sum_total - sum_total * 25 / 100

end_price = sum_total - (sum_total * 10 / 100)

if end_price >= vacation_price:
    sum_left = end_price - vacation_price
    print(f"Yes! {sum_left:.2f} lv left.")

else:
    end_price < vacation_price
    needed_sum = vacation_price - end_price
    print(f"Not enough money! {needed_sum:.2f} lv needed.")

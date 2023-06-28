# Read User Input
days_holiday = int(input())
type_room = input()
feedback = input()

total_price = 0
nights_sleep = days_holiday - 1

if type_room == "room for one person":
    price_per_night = 18.00
    total_price = nights_sleep * price_per_night

elif type_room == "apartment":
    price_per_night = 25.00
    total_price = nights_sleep * price_per_night
    if days_holiday < 10:
        total_price -= total_price * 30 / 100
    elif days_holiday >= 10 and days_holiday<= 15:
        total_price -= total_price * 35 / 100
    else:
        total_price -= total_price * 50 / 100

elif type_room == "president apartment":
    price_per_night = 35.00
    total_price = nights_sleep * price_per_night
    if days_holiday < 10:
        total_price -= total_price * 10 / 100
    elif days_holiday >= 10 and days_holiday <= 15:
        total_price -= total_price * 15 / 100
    else:
        total_price -= total_price * 20 / 100

if feedback == "positive":
    total_price += total_price * 25 / 100
else:
    total_price -= total_price * 10 / 100

print(f"{total_price:.2f}")

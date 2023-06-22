
budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

price_video_card = 250
sum_video = video_card * price_video_card

price_processor = sum_video * 35 / 100
price_ram = sum_video * 10 / 100

sum_processor = processor * price_processor
sum_ram = ram * price_ram

total_price = sum_video + sum_processor + sum_ram

if video_card > processor:
    total_price -= total_price * 15 / 100

money_left = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")


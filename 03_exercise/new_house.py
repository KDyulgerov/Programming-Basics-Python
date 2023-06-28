# Read User Input

type_flower = input()
count_flowers = int(input())
budget = int(input())
price = 0

if type_flower == "Roses":
    price = 5.00
    if count_flowers > 80:
        price -= price * 10 / 100
elif type_flower == "Dahlias":
    price = 3.80
    if count_flowers > 90:
        price -= price * 15 / 100
elif type_flower == "Tulips":
    price = 2.80
    if count_flowers > 80:
        price -= price * 15 / 100
elif type_flower == "Narcissus":
    price = 3.00
    if count_flowers < 120:
        price += price * 15 / 100
elif type_flower == "Gladiolus":
    price = 2.50
    if count_flowers < 80:
        price += price * 20 / 100

price_flowers = price * count_flowers

remain_price = abs(budget - price_flowers)

if budget >= price_flowers:
    print(f"Hey, you have a great garden with {count_flowers} {type_flower} and {remain_price:.2f} leva left.")
elif budget < price_flowers:
    print(f"Not enough money, you need {remain_price:.2f} leva more.")
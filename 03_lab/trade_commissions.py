# Read User Input

town = input()
sum = float(input())

price = "error"
if town == "Sofia":
    if sum >= 0 and sum <= 500:
        price = sum * 5 / 100
    if sum > 500 and sum <= 1000:
        price = sum * 7 / 100
    if sum > 1000 and sum <= 10000:
        price = sum * 8 / 100
    if sum > 10000:
        price = sum * 12 / 100

if town == "Varna":
    if sum >= 0 and sum <= 500:
        price = sum * 4.5 / 100
    if sum > 500 and sum <= 1000:
        price = sum * 7.5 / 100
    if sum > 1000 and sum <= 10000:
        price = sum * 10 / 100
    if sum > 10000:
        price = sum * 13 / 100

if town == "Plovdiv":
    if sum >= 0 and sum <= 500:
        price = sum * 5.5 / 100
    if sum > 500 and sum <= 1000:
        price = sum * 8 / 100
    if sum > 1000 and sum <= 10000:
        price = sum * 12 / 100
    if sum > 10000:
        price = sum * 14.5 / 100

if price == "error":
    print(price)
else:
    print(f"{price:.2f}")
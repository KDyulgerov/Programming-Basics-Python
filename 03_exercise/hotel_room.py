# Read User Input

month = input()
count_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < count_nights <= 14:
        studio -= studio * 5 / 100
    if count_nights > 14:
        studio -= studio * 30 / 100
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if count_nights > 14:
        studio -= studio * 20 / 100
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if count_nights > 14:
    apartment -= apartment * 10 / 100

total_price_studio = studio * count_nights
total_price_apartment = apartment * count_nights
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")

# Read User Input

budget = float(input())
season = input()

destination = " "
type_vacation = " "
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 30 / 100
        type_vacation = "Camp"
    elif season == "winter":
        price = budget * 70 / 100
        type_vacation = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 40 / 100
        type_vacation = "Camp"
    elif season == "winter":
        price = budget * 80 / 100
        type_vacation = "Hotel"

elif budget > 1000:
    destination = "Europe"
    price = budget * 90 / 100
    type_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price:.2f}")
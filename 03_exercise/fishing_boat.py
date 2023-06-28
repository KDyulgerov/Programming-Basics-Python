# Read User Input

budget_of_group = int(input())
season = input()
count_fishers = int(input())

rent = 0

# Logic
if season == "Spring":
    rent = 3000
    if count_fishers <= 6:
        rent -= rent * 10 / 100
    elif 7 <= count_fishers <= 11:
        rent -= rent * 15 / 100
    elif count_fishers > 12:
        rent -= rent * 25 / 100

elif season == "Summer" or season == "Autumn":
    rent = 4200
    if count_fishers <= 6:
        rent -= rent * 10 / 100
    elif 7 <= count_fishers <= 11:
        rent -= rent * 15 / 100
    elif count_fishers > 12:
        rent -= rent * 25 / 100

elif season == "Winter":
    rent = 2600
    if count_fishers <= 6:
        rent -= rent * 10 / 100
    elif 7 <= count_fishers <= 11:
        rent -= rent * 15 / 100
    elif count_fishers > 12:
        rent -= rent * 25 / 100

if count_fishers % 2 == 0 and season != "Autumn":
    rent -= rent * 5 / 100

remain_balance = abs(budget_of_group - rent)

if budget_of_group >= rent:
    print(f"Yes! You have {remain_balance:.2f} leva left.")
elif budget_of_group < rent:
    print(f"Not enough money! You need {remain_balance:.2f} leva.")


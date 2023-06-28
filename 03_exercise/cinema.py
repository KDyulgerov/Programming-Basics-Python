# Read User Input
type = input()
rows = int(input())
colms = int(input())

hall_area = rows * colms
total_price = 0

if type == "Premiere":
    total_price = hall_area * 12.00

elif type == "Normal":
        total_price = hall_area * 7.50

elif type == "Discount":
        total_price = hall_area * 5.00

print(f"{total_price:.2f} leva")


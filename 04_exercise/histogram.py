# Read User Input
numbers = int(input())

count_p1, count_p2, count_p3, count_p4, count_p5 = 0, 0, 0, 0, 0
# Logic
for i in range(numbers):
    count_number = int(input())

    if count_number < 200:
        count_p1 += 1
    elif count_number <= 399:
        count_p2 += 1
    elif count_number <= 599:
        count_p3 += 1
    elif count_number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

sum_p1 = count_p1 / numbers * 100
sum_p2 = count_p2 / numbers * 100
sum_p3 = count_p3 / numbers * 100
sum_p4 = count_p4 / numbers * 100
sum_p5 = count_p5 / numbers * 100

# Output

print(f"{sum_p1:.2f}%")
print(f"{sum_p2:.2f}%")
print(f"{sum_p3:.2f}%")
print(f"{sum_p4:.2f}%")
print(f"{sum_p5:.2f}%")
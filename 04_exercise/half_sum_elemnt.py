# Read User Input
import sys

count_numbers = int(input())

sum_numbers = 0
max_numbers = -sys.maxsize

# Logic
for i in range(0, count_numbers):
    num = int(input())
    if num > max_numbers:
        max_numbers = num
    sum_numbers += num

sum_numbers = sum_numbers - max_numbers
if max_numbers == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {abs(max_numbers - sum_numbers)}")


# Output

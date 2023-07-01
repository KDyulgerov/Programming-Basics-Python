# Read User Input
number = int(input())
left_sum = 0
right_sum = 0

# Logic
for i in range(number):
    user_input = int(input())
    left_sum += user_input

for i in range(number):
    user_input = int(input())
    right_sum += user_input

# Output
diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")

else:
    print(f"No, diff = {diff}")
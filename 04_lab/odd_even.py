# Reda User Input
number = int(input())

even_sum = 0
odd_sum = 0

# Logic
for i in range(number):
    user_input = int(input())

    if i % 2 == 0:
        even_sum += user_input
    else:
        odd_sum += user_input

diff = abs(odd_sum - even_sum)

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {diff}")



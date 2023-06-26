# Read user input
number = int(input())

result = " "

# Logic
if number >= -100 and number <= 100 and number != 0:
    result = "Yes"
else:
    result = "No"

# Output
print(result)
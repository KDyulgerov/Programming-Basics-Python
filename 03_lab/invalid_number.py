# Read User Input

number = int(input())
result = " "

# Logic
is_number_valid = (number >= 100 and number <= 200) or number == 0

if not is_number_valid:
    print("invalid")

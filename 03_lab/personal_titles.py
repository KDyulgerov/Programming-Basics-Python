
# Read user input
age = float(input())
gender = input()

result = " "

# Logic
if gender == "m":
    if age >= 16:
        result = "Mr."
    else:
        result = "Master"
else:
    gender == "f"
    if age >= 16:
        result = "Ms."
    else:
        result = "Miss"

# Output
print(result)
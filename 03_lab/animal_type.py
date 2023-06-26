# Read user input

type = input()

result = " "

# Logic
if type == "dog":
    result = "mammal"
elif type == "tortoise" or type == "snake" or type == "crocodile":
    result = "reptile"
else:
    result = "unknown"

# Output
print(result)
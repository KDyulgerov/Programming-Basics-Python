# Read user input
hour = int(input())
day_of_week = input()

result = " "
# Logic
if (hour >= 10 and hour <= 18) and (day_of_week == "Monday" or day_of_week == "Tuesday" \
or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" \
or day_of_week == "Saturday"):
    result = "open"
elif day_of_week == "Sunday":
    result = "closed"
else:
    result = "Error"

# Output
print(result)
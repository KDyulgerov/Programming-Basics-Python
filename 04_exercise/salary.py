# Read User Input

tab_opens = int(input())
salary = int(input())

# Logic
for i in range(tab_opens):
    sites = input()
    if sites == "Facebook":
        salary -= 150
    elif sites == "Instagram":
        salary -= 100
    elif sites == "Reddit":
        salary -= 50
    if salary <= 0:
        break

# Output
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")


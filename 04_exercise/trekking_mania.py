# Read User Input
number_of_groups = int(input())

group_of_5 = 0
group_of_6_12 = 0
gropu_of_13_25 = 0
group_of_26_40 = 0
group_of_41plus = 0
total_people = 0

# Logic
for i in range(number_of_groups):
    count_people = int(input())
    total_people = total_people + count_people

    if count_people <= 5:
        group_of_5 += count_people
    elif 6 <= count_people <= 12:
        group_of_6_12 += count_people
    elif 13 <= count_people <= 25:
        gropu_of_13_25 += count_people
    elif 26 <= count_people <= 40:
        group_of_26_40 += count_people
    elif count_people > 40:
        group_of_41plus += count_people

    # Output

print(f"{group_of_5 / total_people * 100:.2f}%")
print(f"{group_of_6_12 / total_people * 100:.2f}%")
print(f"{gropu_of_13_25 / total_people * 100:.2f}%")
print(f"{group_of_26_40 / total_people * 100:.2f}%")
print(f"{group_of_41plus / total_people * 100:.2f}%")

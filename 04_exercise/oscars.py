# Read User Input
name_actor = input()
academy_points = float(input())
number_jury = int(input())

limit = 1250.5
total_points = 0
sum_points = 0
# Logic
for i in range(number_jury):
    name_jury = input()
    points_jury = float(input())

    points_name = len(name_jury)
    sum_points += points_name * points_jury / 2
    total_points = sum_points + academy_points

    if total_points > limit:
        break

diff = abs(total_points - limit)

# Output
if total_points > limit:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")

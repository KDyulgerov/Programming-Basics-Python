from math import floor

# Read User Input
tournaments_number = int(input())
starting_points = int(input())

W = 2000
F = 1200
SF = 720
total_points = 0
winner = 0
average_count = 0
# Logic
for i in range(tournaments_number):
    stage = input()

    if stage == "W":
        total_points += W
        average_count += W
        winner += 1
    elif stage == "F":
        total_points += F
        average_count += F
    elif stage == "SF":
        total_points += SF
        average_count += SF

    sum_points = total_points + starting_points
    average = average_count / tournaments_number
    winner_percentage = (winner / tournaments_number) * 100
# Output

print(f"Final points: {sum_points}")
print(f"Average points: {floor(average)}")
print(f"{winner_percentage:.2f}%")


points = int(input())

bonus = 0
if points <= 100:
    bonus = 5

if points > 100:
    bonus = points * 20 / 100

if points > 1000:
    bonus = points * 10 / 100

if points % 2 == 0:
    bonus += 1
elif points % 10 == 5:
    bonus += 2

print(bonus)
print(points + bonus)


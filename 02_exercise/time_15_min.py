
hours = int(input())
minutes = int(input())

min_per_hour = hours * 60
total_min = min_per_hour + minutes + 15

sum_hours = total_min // 60
sum_minutes = total_min % 60

if sum_hours > 23:
    sum_hours = 0

if sum_minutes < 10:
    print(f"{sum_hours}:0{sum_minutes}")

else:
    print(f"{sum_hours}:{sum_minutes}")
import math
name_tv = input()
duration_series = int(input())
duration_break = int(input())

lunch_time = duration_break / 8
relax_time = duration_break / 4

time_left = duration_break - lunch_time - relax_time

time_left_break = abs(time_left - duration_series)

if time_left >= duration_series:
    print(f"You have enough time to watch {name_tv} and left with {math.ceil(time_left_break)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_tv}, you need {math.ceil(time_left_break)} more minutes.")
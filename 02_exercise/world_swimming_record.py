import math

record_sec = float(input())
distance_meters = float(input())
time_sec_per_meter = float(input())

swim_distance = distance_meters * time_sec_per_meter
slower_time = math.floor(distance_meters / 15) * 12.5

total_time = swim_distance + slower_time

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    total_time > record_sec
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")


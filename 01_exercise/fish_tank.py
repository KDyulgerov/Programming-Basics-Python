
length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_aquarium = length * width * height
volume_liters = volume_aquarium * 0.001
prostranstvo = percentage / 100
liters_needs = volume_liters * (1 - prostranstvo)

print(liters_needs)

from math import pi

figure = input()

if figure == "square":
    size = float(input())
    area = size * size
    print(f"{area:.3f}")

elif figure == "rectangle":
    size = float(input())
    size_2 = float(input())
    area = size * size_2
    print(f"{area:.3f}")

elif figure == "circle":
    size = float(input())
    area = pi * size * size
    print(f"{area:.3f}")

elif figure == "triangle":
    size = float(input())
    size_2 = float(input())
    area = size * size_2 / 2
    print(f"{area:.3f}")


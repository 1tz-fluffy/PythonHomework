import math

a = float(input())
b = float(input())
c = float(input())

d = b**2 - 4*a*c

if d > 0:
    x = (-b + math.sqrt(d)) / (2*a)
    y = (-b - math.sqrt(d)) / (2*a)
    print(x, y)
elif d == 0:
    x = -b / (2*a)
    print(x)
else:
    print("Корней нет")

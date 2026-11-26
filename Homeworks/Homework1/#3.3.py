import math

a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

if d > 0:
    e = (-b + math.sqrt(d)) / (2 * a)
    f = (-b - math.sqrt(d)) / (2 * a)
    print(e, f)
elif d == 0:
    e = -b / (2 * a)
    print(e)
else:
    print("Корней нет")

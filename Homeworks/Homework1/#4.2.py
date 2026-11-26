def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

a = float(input())
b = float(input())
c = float(input())
print(min_of_three(a, b, c))

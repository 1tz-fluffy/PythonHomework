def power_count(base, exponent):
    a = 1
    for b in range(exponent):
        a *= base
    return a

a = int(input())
b = int(input())
c = power_count(a, b)
print(f"{a} в степени {b} = {c}")

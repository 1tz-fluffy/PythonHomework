def RootK(x, k, n):
    if n == 0:
        return 1
    a = RootK(x, k, n - 1)
    return a - (a - x / (a ** (k - 1))) / k

print(RootK(8, 3, 1))
print(RootK(8, 3, 2))
print(RootK(8, 3, 3))
print(RootK(8, 3, 4))
print(RootK(8, 3, 5))
print(RootK(8, 3, 6))
print(RootK(8, 3, 7))
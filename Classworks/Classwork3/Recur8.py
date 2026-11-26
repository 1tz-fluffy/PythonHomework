def RootK(X, K, N):
    if N == 0:
        return 1
    a = RootK(X, K, N - 1)
    return a - (a - X / (a ** (K - 1))) / K

print(RootK(8, 3, 2))
print(RootK(16, 2, 4))
print(RootK(81, 4, 3))
print(RootK(25, 2, 5))

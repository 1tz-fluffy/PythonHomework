a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def fib2(n):
    if a[n] == 1 or a[n] == 2:
        return 1
    elif a[n] != 0:
        return a[n]
    return fib2(n - 1) + fib2(n - 2)


b = int(input())
print(fib2(b))

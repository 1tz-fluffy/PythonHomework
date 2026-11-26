a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0


def fib2(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    elif a[n] != 0:
        return a[n]
    a[n] = fib2(n - 1) + fib2(n - 2)
    return a[n]


b = int(input())
print(fib2(b))
print("Вызовов: ", count)

a = int(input())
b = a // 100
c = (a // 10) % 10
d = a % 10
e = b + c + d

if e % 2 == 0:
    print("Сумма цифр чётная")
else:
    print("Сумма цифр нечётная")

num = int(input("Введите трехзначное число: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

z = a + b + c

if z % 2 == 0:
    print("Сумма цифр чётная")
else:
    print("Сумма цифр нечётная")

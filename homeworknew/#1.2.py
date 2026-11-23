a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    mx = a
elif b >= a and b >= c:
    mx = b
else:
    mx = c

print("Наибольшее число:", mx)

a = input()
if a.isdigit():
    b = int(a)
    c = 0
    for d in str(b):
        c += int(d)
    print(c)
else:
    print("Не число")

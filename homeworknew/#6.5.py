a = int(input("amount: "))
b = []
for c in range(0, a):
    d = input()
    b.append(d)

for e, f in enumerate(b):
    if e % 2 == 0:
        print(e, f)

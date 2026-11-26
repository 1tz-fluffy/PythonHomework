a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

for e in range(len(b)):
    if b[e] % 7 == 0:
        print(e)
        break

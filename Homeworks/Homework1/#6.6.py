a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

e = sum(b) / len(b)
f = [g for g in b if g < e]
print(f)

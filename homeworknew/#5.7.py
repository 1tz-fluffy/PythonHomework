a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

e = len(b) // 2
f = b[e:] + b[:e]
print(f)

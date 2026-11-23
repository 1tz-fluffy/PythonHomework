a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

e = []
f = 0

while f < len(b):
    if b[f] < 0:
        e.append(b.pop(f))
    else:
        f += 1

print(b)
print(e)

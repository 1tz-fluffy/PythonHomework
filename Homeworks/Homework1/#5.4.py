a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

b.insert(2, 0)
print(b)
b.remove(0)
print(b)

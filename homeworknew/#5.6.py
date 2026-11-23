a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

b.reverse()
print(b[::2])

a = int(input("amount: "))
b = []
for c in range(0, a):
    d = int(input())
    b.append(d)

e = b[:1] + b[1:-1][::-1] + b[-1:]
print(e)

a = int(input("amount: "))
b = []
for c in range(0, a):
    d = input()
    b.append(d)

e = [f for f in b if f[0] == "А" or f[0] == "а"]
print(e)

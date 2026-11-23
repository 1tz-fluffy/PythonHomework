a = input()
b = int(input("кол-во запрещенных слов: "))
c = []
for d in range(0, b):
    e = input()
    c.append(e)

for f in c:
    a = a.replace(f, "*")

print(a)

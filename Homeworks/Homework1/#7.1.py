a = input().lower()
b = "ауеёыяиюэй"
c = 0

for d in a:
    if d in b:
        c += 1

print(c)

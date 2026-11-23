def total_score(*points, bonus=0):
    a = sum(points) + bonus
    if a < 0:
        return 0
    else:
        return a
pass
print(total_score(10, -15, 20, bonus=5))  # Ожидается: 20
print(total_score(5, -20, bonus=0))  # Ожидается: 0

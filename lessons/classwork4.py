def check_password(password):
    a = password
    if len(a) < 6 or a.isdigit():
        return "Слабый"
    else:
        return "Нормальный"
pass

print(check_password("1234567"))  # Ожидается: "Слабый"
print(check_password("kot2026"))  # Ожидается: "Нормальный"

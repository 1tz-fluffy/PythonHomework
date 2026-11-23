def power_count(base, exponent):
    d = 1
    for i in range(exponent):
        d = d * base
    print(f"{base} в степени {exponent} равно {d}")

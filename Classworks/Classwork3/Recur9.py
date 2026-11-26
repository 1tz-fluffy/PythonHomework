def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)

print(GCD(30, 6))
print(GCD(50, 25))
print(GCD(89, 19))
print(GCD(121, 33))

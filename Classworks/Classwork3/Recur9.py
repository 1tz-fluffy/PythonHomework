def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)

print(GCD(48, 18))
print(GCD(100, 25))
print(GCD(17, 13))
print(GCD(81, 54))

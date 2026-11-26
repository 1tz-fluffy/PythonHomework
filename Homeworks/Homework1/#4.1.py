def is_prime(n):
    if n < 2:
        return False
    for a in range(2, n):
        if n % a == 0:
            return False
    return True

a = int(input())
print(is_prime(a))

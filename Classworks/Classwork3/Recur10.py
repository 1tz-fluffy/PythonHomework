def DigitSum(K):
    if K == 0:
        return 0
    return (K % 10) + DigitSum(K // 10)

print(DigitSum(123))
print(DigitSum(4567))
print(DigitSum(90))
print(DigitSum(5))
print(DigitSum(888))

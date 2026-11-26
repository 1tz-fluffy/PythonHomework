def DigitSum(K):
    if K == 0:
        return 0
    return (K % 10) + DigitSum(K // 10)

print(DigitSum(1234))
print(DigitSum(321))
print(DigitSum(60))
print(DigitSum(5))
print(DigitSum(999))

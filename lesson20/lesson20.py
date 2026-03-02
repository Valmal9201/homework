# Lesson 20
num = range(1, 10000)
totalSum = 0
total = 0
for i in num:
    divisor = 1
    quotient = 0
    while divisor < i:
        if i % divisor == 0:
            quotient == i // divisor
            if quotient == divisor:
                total += divisor
            else:
                total = total + quotient + divisor
        divisor += 1
    if total == i:
        totalSum += total
    total = 0
    i += 1
print(totalSum)
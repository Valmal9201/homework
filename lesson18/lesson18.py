# Lesson 18
num = int(input())
i = 1
num1 = range(1, num + 1)

for i in num1:
    if num % i == 0:
        print(i)
    i += 1
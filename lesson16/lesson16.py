# Lesson 16
num = range(1, 51)
for i in num:
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i}: Fizzbuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
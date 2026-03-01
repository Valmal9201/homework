# Lesson 17
num = int(input("Enter your number: "))
i = num
factorial = 1

while i > 1:
    factorial *= i
    i -= 1

print(f"The factorial of {num} is {factorial}.")

# Lesson 4
import math
count = 0
fence  = 0
while (count < 3):
    fence += len((input("Enter the length of the fence in F's: ex (3 = FFF): ")))
    count += 1

cans = math.ceil(fence/12)
print (f"{fence}\n{(cans * 12 - fence) % 12}\n{cans * 14.90}")
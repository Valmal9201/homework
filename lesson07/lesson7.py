# Lesson 7
from random import randrange
dc = int(input("Enter the DC: "))
ran = randrange(1, 21)

print(f"D20 roll: {ran}")
if (ran < dc):
    print("Failed Check")
else:
    print ("Passed Check")
# Lesson 10
num = input("Enter the last 4 digits of the number: ")
if num[0] == "8" or num[0] == "9":
    if num[-1] == "8" or num[-1] == "9":
        if num[1] == num[2]:
            print("Telemarketer")
else:
    print("Not a telemarketer")
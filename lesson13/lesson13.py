# Lesson 13
month = int(input("Enter month as number (Ex. 1 = Jan, 12 = Dec): "))
day = int(input("Enter day as number: "))

if month > 0 and month < 13 and day > 0 and day < 32:
    if month <= 2:
        if (month == 2 and day < 18) or month == 1:
            print("Before")
        elif month == 2 and day == 18:
            print("Special")
        elif month == 2 and (19 <= day <= 29):
            print("After")  
    elif month >= 3 and month <= 12:
        print("After")
else:
    print("Not a date.")
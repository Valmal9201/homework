# Lesson 12
a = int(input("Enter Angle A: "))
b = int(input("Enter Angle B: "))
c = int(input("Enter Angle C: "))

if a + b + c == 180:
    if a == b == c == 60:
        print("Equilateral Triangle")
    elif a != b != c:
        print("Scalene Triangle")
    else:
        print("Isosceles Triangle")
else:
    print("Not Triangle")
# Lesson 5
money = float(input("Enter starting money: $"))
cookie = input("Enter cookies as letters (b = big, c = small): ")
small = 0
big = 0
profit = 0
totalCookies = cookie.count("c") + cookie.count("b")

for i in cookie:
    if i == "c":
        small += 1
        profit += 0.75
    elif i == "b":
        big += 1
        profit += 1.25
    else:
        print(f"{i} is not a valid item.")
print(f"Cookies sold: {totalCookies}\nProfit: ${profit}\nFinal Amount: ${profit + money}")
# Lesson 19
# 1
num = int(input())
i = 2
ctr = 0

while i < num:
    if num % i == 0:
        ctr += 1
        break
    i += 1

if ctr > 0:
    print("Composite")
else:
    print("Prime")

# 2
num = int(input())
i = 2
stop = num ** 0.5
ctr = 0

while i < stop:
    if num % i == 0:
        ctr += 1
        break
    i += 1

if ctr > 0:
    print("Composite")
else:
    print("Prime")
# Lesson 8
i = 0
game = ""

for i in range(6):
    result = input("Enter the result of the game (W = Win, L = Lose): ")
    while result != "W" and result != "L":
        print("Invalid result")
        result = input("Try again. Enter the result of the game (W = Win, L = Lose): ")
    game += result    
    i += 1
wins = game.count("W")

if (wins >= 5):
    print("Group 1")
elif (wins >= 3):
    print("Group 2")
elif (wins >= 1):
    print("Group 3")
else:
    print("Eliminated")
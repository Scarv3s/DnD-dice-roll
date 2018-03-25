from random import randint

D20 = randint(1, 20)
D10 = randint(1, 10)
D8 = randint(1, 8)
D6 = randint(1, 6)
D4 = randint(1, 4)
dice = ["d20", "d10", "d8", "d6", "d4", "D20", "D10", "D8", "D6", "D4"]

def roll(choice):
    if choice in ("D20", "d20"):
        print(D20)
    elif choice in ("D10", "d10"):
        print(D10)
    elif choice in ("D8", "d8"):
        print(D8)
    elif choice in ("D6", "d6"):
        print(D6)
    elif choice in ("D4", "d4"):
        print(D4)
        
x = input("Dice: ")
check = True
while check:
    check = False
    if x in dice:
        check = True
        roll(x)
        break
    else:
        check = True
        print("Sorry, I didn't quite catch that.")
        x = input("Pick a dice: ")
        roll(x)
        




"""
if choice == "D20" or choice == "d20":
    print(D20)
elif choice == "D10" or choice == "d10":
    print(D10)
elif choice == "D8" or choice == "d8":
    print(D8)
elif choice == "D6" or choice == "d6":
    print(D6)
elif choice == "D4" or choice == "d4":
    print(D4)
else:
    print("I'm sorry, I didn't quite get that")
    choice = input( )
"""
#Treasure game using if else.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

way = input("Choose your way. Left or Right\n")         #variable.lower() function can also be used instead of giving different lowercase words.

if way == "Right" or way == "RIGHT" or way == "right":
    print("You have choosen the Right path and fell into a hole\nGame Over")

if way == "Left" or way == "LEFT" or way == "left":
    way1 = input("Do you want to wait or swim the river\n")

    if way1 == "Swim" or way1 == "SWIM" or way1 == "swim":
        print("You were attacked by crocodiles\nGame Over")

    if way1 == "Wait" or way1 == "WAIT" or way1 == "wait":
        door = input("Which Door will you choose Red, Blue, Yellow?\n")

        if door == "Red" or door == "RED" or door == "red":
            print("You were burned by fire\nGame Over")

        if door == "Blue" or door == "BLUE" or door == "blue":
            print("You were eaten by beasts\nGame Over")

        if door == "Yellow" or door == "YELLOW" or door == "yellow":
            print("You win")

        else:
            print("You choose the door that does not exists\nGame Over")

else:
    print("Game Over")
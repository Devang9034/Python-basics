import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
choice = int(input("Select 0 for Rock, Select 1 for Paper and Select 2 for Scissors\n"))

if choice >= 3 or choice < 0:
    print("Invalid Response")

else:
    print(game_image[choice])

# if choice == 0:               #This is the other method if you do not want to use list
#     print(rock)

# if choice == 1:
#     print(paper)

# if choice == 2:
#     print(scissors)

random = random.randint(0, 2)
print("Computer: ")

if random == 0:
    print(rock)

if random == 1:
    print(paper)

if random == 2:
    print(scissors)

#Now if else statements for winner.

if choice == 0 and random == 2:
    print("You Win!")

if choice == 1 and random == 0:
    print("You Win!")

if choice == 2 and random == 1:
    print("You Win!")

if choice == 2 and random == 0:
    print("You lose!")

if choice == 0 and random == 1:
    print("You lose!")

if choice == 1 and random == 2:
    print("You lose!")

if choice == random:
    print("Its a draw")
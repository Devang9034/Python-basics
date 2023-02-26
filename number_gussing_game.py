#Number Guessing Game
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print(logo)
number = random.choice(list)

mode = input("Select the mode, for easy press 'e' and for hard press 'h': ")

def game():
	if mode == "e":
		print("You have 10 attempts to guess the number.")

		for _ in range(10):
			guess = int(input("Enter the number that I am thinking between 1 and 100: "))
			if guess < number:
				print("Too Low")

			if guess > number:
				print("Too High")

			if guess == number:
				print(f"You won, The Number was {number}")
				return

	if mode == "h":
		print("You have 5 attempts to guess the number.")
		
		for _ in range(5):
			guess = int(input("Enter the number that I am thinking between 1 and 100: "))
			if guess < number:
				print("Too Low")

			if guess > number:
				print("Too High")

			if guess == number:
				print(f"You won, The Number was {number}")
				return

	print(f"The Number was {number}")

game()
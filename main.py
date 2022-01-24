# Name: Ruben Sanduleac
# Description: This is a number guessing game that gives the user the choice to pick the
#              difficulty of the game.

import random

attempts = 0
game_over = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == 'easy':
    attempts = 10
elif diff == 'hard':
    attempts = 5
number = random.randint(1, 100)

while not game_over and not attempts == 0:
    guess = int(input("Make a guess: "))
    if number > guess:
        print("Too low.")
    elif number < guess:
        print("Too high")
    elif number == guess:
        print("You Guessed It!")
        break
    else:
        print("Invalid input.")

    attempts -= 1

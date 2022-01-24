# Name: Ruben Sanduleac
# Description: This is a number guessing game that gives the user the choice to pick the
#              difficulty of the game.

import random
from background import logo
from clear_func import clear

attempts = 0
game_over = False
run_again = True

print(logo)
print("Welcome to the Number Guessing Game!")

while run_again:
    print("I'm thinking of a number between 1 and 100.")
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
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
        print(f"Attempts Left [{attempts}] ")
    print("Sorry you ran out of attempts.")
    run_again = input(
        "Do you want to try again: Type 'y' yes and 'n' for no: ").lower()
    if run_again == 'y':
        run_again = True
        clear()
    else:
        run_again = False

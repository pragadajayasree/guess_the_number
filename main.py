#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random
from replit import clear


def leftattempts(left):
    print(f"You have {left} attempts remaining to guess the number")


def makeguess():
    guess = int(input("Make a guess: "))
    return guess


def guess_num():
    print(art.logo)
    print("welcome to number guessing game")
    print("I am thinking of a number between 1 and 100")
    num = random.randint(1, 100)
    choice = input("choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        left = 10

        while (left >= 1):
            leftattempts(left)
            guess = makeguess()
            if guess > num:
                print("Too high")
                print("guess again")
                left -= 1

            elif guess < num:
                print("Too low")
                print("guess again")
                left -= 1

            elif guess == num:
                print(f"you got it. the answer is {num}")
                break
        if left < 1:
            print("you have run out of guesses. You lose")

    elif choice == "hard":
        left = 5

        while (left >= 1):
            leftattempts(left)
            guess = makeguess()
            if guess > num:
                print("Too high")
                print("guess again")
                left -= 1

            elif guess < num:
                print("Too low")
                print("guess again")
                left -= 1

            elif guess == num:
                print(f"you got it. the answer is {num}")
                break
        if left < 1:
            print("you have run out of guesses. You lose")


guess_num()

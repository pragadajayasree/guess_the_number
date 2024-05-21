import art
import random


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

        while left >= 1:
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

        while left >= 1:
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

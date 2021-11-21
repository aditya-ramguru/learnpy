import random
import ART
from enum import IntEnum


class Difficulty(IntEnum):
    easy = 10
    hard = 5


def game():
    print(ART.logo)
    print("Welcome to the Number guessing game!\nI'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)

    print(f"Psst the answer is {answer}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    attempts = Difficulty[difficulty].value
    print(f"You have {attempts} lives")

    guess = int(input("Make a Guess: "))

    while attempts >= 1:
        if guess == answer:
            print(f"you got the right answer the number was {answer}")
            break
        elif guess < answer:
            print("Too low")
        else:
            print("Too High")

        if attempts > 1:
            print(f'You have {attempts-1} lives remaining')

        if guess != answer and attempts == 1:
            print(f"YOU LOSE    GAME OVER!\nThe number was {answer}")
            break

        attempts -= 1
        guess = int(input("Guess again: "))

    play_again = input("Would you like to play again. Type 'y' for yes and 'n' for no: ")
    if play_again == 'y':
        game()
    else:
        print("END")


game()











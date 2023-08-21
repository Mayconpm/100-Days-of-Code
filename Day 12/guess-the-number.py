import random
from os import system

from art import logo


def main():
    system("cls")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 101)
    attempts_number = choose_dificult()
    guess_game(attempts_number, number)


def choose_dificult():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        attempts_number = 5
    else:
        attempts_number = 10
    return attempts_number


def guess_game(attempts_number, number):
    print(f"You have {attempts_number} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        exit()
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")
    if attempts_number > 1:
        print("Guess again.")
        guess_game(attempts_number - 1, number)
    else:
        print("You've run out of guesses, you lose.")
    


if __name__ == "__main__":
    main()

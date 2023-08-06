import random

import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = ["_"] * len(chosen_word)
lives = 6

print(display)
print(hangman_art.logo)

play = True
while play:
    wrong_guess = True
    guess = input("Guess a letter: ").lower()

    for i, letter in enumerate(chosen_word):
        if letter == guess and letter not in display:
            wrong_guess = False
            display[i] = guess

    print(" ".join(display))
    print(hangman_art.stages[lives])

    if wrong_guess:
        lives -= 1

    if "_" not in display:
        play = False
        print("You won!!!")
    elif lives < 0:
        play = False
        print("You lose!!!")

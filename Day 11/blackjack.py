from os import system
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards_score):
    if sum(cards_score) == 21 and len(cards_score) == 2:
        score = 0
    else:
        score = sum(cards_score)
    return score


def final_hand(player_cards, computer_cards, player_score, computer_score):
    print(f"Your final hand: {player_cards} final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")


def play_computer(computer_cards, computer_score):
    while computer_score < 17:
        computer_score = calculate_score(computer_cards)
        computer_cards.append(random.choice(cards))
    return computer_cards, computer_score


def compare_scores(player_score, computer_score):
    if player_score == 0:
        print("Win with a Blackjack 😎")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif player_score > 21:
        print("You went over. You lose 😭")
    elif player_score == computer_score:
        print("Draw 🙃")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score > computer_score:
        print("You win 😃")
    elif computer_score > player_score:
        print("You lose 😤")


def deal_player(player_cards, player_score, computer_cards):
    continue_playing = True
    while continue_playing:
        if player_score < 21:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == "y":
                player_cards.append(random.choice(cards))
                player_score = calculate_score(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            else:
                continue_playing = False
        else:
            continue_playing = False
    return player_cards, player_score


def play_blackjack():
    player_cards = random.choices(cards, k=2)
    player_score = calculate_score(player_cards)

    computer_cards = random.choices(cards, k=2)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    player_cards, player_score = deal_player(player_cards, player_score, computer_cards)

    computer_cards, computer_score = play_computer(computer_cards, computer_score)

    final_hand(player_cards, computer_cards, player_score, computer_score)

    compare_scores(player_score, computer_score)


def main():
    should_play = True
    while should_play:
        want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if want_play == "y":
            system("cls")
            print(logo)
            play_blackjack()


if __name__ == "__main__":
    system("cls")
    main()

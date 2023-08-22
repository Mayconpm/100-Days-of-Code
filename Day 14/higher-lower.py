import random
from os import system

from art import logo, vs
from game_data import data


def main():
    system("cls")
    print(logo)
    score = 0
    candidate_a = random.choice(data)
    keep_playing = True
    while keep_playing:
        candidate_b = random.choice(data)
        followers_a = candidate_a["follower_count"]
        followers_b = candidate_b["follower_count"]
        bigger = check_bigger(followers_a, followers_b)
        print(f"Compare A: {format_data(candidate_a)}.")
        print(vs)
        print(f"Compare B: {format_data(candidate_b)}.")
        player_guess = input("Who has more followers? Type 'A' or 'B':").upper()
        system("cls")
        if player_guess == bigger:
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}.")
            candidate_a = candidate_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False


def check_bigger(followers_a, followers_b):
    if followers_a > followers_b:
        bigger = "A"
    else:
        bigger = "B"
    return bigger


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


if __name__ == "__main__":
    main()

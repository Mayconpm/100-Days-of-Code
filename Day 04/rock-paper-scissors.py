import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇


game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
    exit()

print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if (
    user_choice == 0
    and computer_choice == 2
    or user_choice == 1
    and computer_choice == 0
    or user_choice == 2
    and computer_choice == 1
):
    print("You won!")
elif (
    user_choice == 1
    and computer_choice == 2
    or user_choice == 0
    and computer_choice == 1
    or user_choice == 2
    and computer_choice == 0
):
    print("You lose!")

elif user_choice == computer_choice:
    print("It's a Draw")

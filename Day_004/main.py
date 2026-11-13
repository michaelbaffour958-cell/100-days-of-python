#BUILDING ROCK, PAPER , SCISSORS  GAME
import random


rock = r"""
    _______
   /       \
  |  ROCK   |
   \_______/
"""

paper = r"""
  _____________
 |             |
 |    PAPER    |
 |_____________|
"""

scissors = r"""
    \\  //
     \\//
     //\\
    (o)(o)
   SCISSORS
"""


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if 0 <= user_choice <= 2:
    print("You chose:")
    print(game_images[user_choice])

    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Please enter a correct input")
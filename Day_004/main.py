#BUILDING ROCK, PAPER , SCISSORS  GAME
import random

choice = ["Rock","Paper","Scissors"]
user_choice = int(input("What do you choose? Enter 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.choice(choice)
if user_choice == 0 and computer_choice == "Rock":
    print("It's a tie!")

elif user_choice == 0 and computer_choice == "Scissors":
    print("You win!")

elif user_choice == 0 and computer_choice == "Paper":
    print("Computer wins!")

elif user_choice == 1 and computer_choice == "Rock":
    print("You win!")

elif user_choice == 1 and computer_choice == "Scissors":
    print("Computer wins!")

elif user_choice == 1 and computer_choice == "Paper":
    print("It's a tie!")

elif user_choice == 2 and computer_choice == "Rock":
    print("Computer wins!")

elif user_choice == 2 and computer_choice == "Scissors":
    print("It's a tie!")

elif user_choice == 2 and computer_choice == "Paper":
    print("You win!")

else:
    print("Please enter a correct input")
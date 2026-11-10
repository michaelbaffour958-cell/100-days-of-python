import random

number = random.randint(0,1)
guess = int(input("Enter your number from 0 to 1: "))
if guess == 0:
    print("Heads")

else:
    print("Tails")
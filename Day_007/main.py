#Building Hangman
import random
d_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(d_list)
print(chosen_word)

user_input = input("Guess the letter of the word: ").lower()
guess = user_input
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

placeholder = []

for letter in chosen_word:
    placeholder += "_"
print(placeholder)

    
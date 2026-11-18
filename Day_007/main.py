#Building Hangman
import random
d_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(d_list)
print(chosen_word)

game_over = False

while not game_over:
 user_input = input("Guess the letter of the word: ").lower()
 guess = user_input
 print(guess)


placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

display = ''
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"
print(display)






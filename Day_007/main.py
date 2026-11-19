#Building Hangman
import random
d_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(d_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_word = []

while not game_over:
 user_input = input("Guess the letter of the word: ").lower()
 guess = user_input
 print(guess)

 display = ''
 for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_word.append(guess)
    elif letter in correct_word:
       display += letter
    else:
        display += "_"
 print(display)

 if "_" not in display:
    game_over = True
    print('You win')






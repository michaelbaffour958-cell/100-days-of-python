#Building Hangman
import random
import hangman_words

HANGMAN = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


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
lives = 6

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
    print('You win.')

 if guess not in chosen_word:
   lives -= 1
   if lives == 0:
      game_over = True
      print("You lose.")


 print(HANGMAN[lives])










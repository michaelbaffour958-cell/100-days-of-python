import random

word_list = ["python", "banana", "teacher", "kumasi", "student", "laptop", "garden"]

stages = [
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
]

chosen_word = random.choice(word_list)
lives = 6
display = ["_"] * len(chosen_word)
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display))

while "_" in display and lives > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    print(" ".join(display))
    print(stages[lives])
    print(f"Lives left: {lives}")

if "_" not in display:
    print("\nYou win!")
else:
    print(f"\nYou lose. The word was '{chosen_word}'.")
import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark","baboon","camel"]

# 1 Create a variable called lives to keep track of how many lives the player has left. The player starts with 6 lives. When lives reaches 0, the game should stop and print "You lose."

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for a in chosen_word:
    placeholder += "_ "
print(f"The word contains \n {placeholder} letters\n")

game_end = False
correct_letters = []

while game_end == False:
    guessed_letter = input(" Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guessed_letter:
            display += letter
            correct_letters += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(f"\n{display}")

    # 2 Reduce the number of lives by one each time the player guesses a letter that is not in the chosen word.

    if guessed_letter not in chosen_word:
        lives -= 1
        print("You lost one life! ")
        print(f"You currently have {lives} lives! ")
        if lives == 0:
            game_end = True
            print("You lose! ")

    if "_" not in display:
        game_end = True
        print("You Win!")

    # 3 Print the ASCII art from the stages list corresponding to the current number of lives remaining.
    print(stages[lives])

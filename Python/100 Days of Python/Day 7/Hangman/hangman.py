import random
import hangman_art
import hangman_words

print("Welcome to Hangman!!!!")

lives = 6

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for a in chosen_word:
    placeholder += "_ "
print(f"The word contains \n {placeholder} letters\n")

game_end = False
correct_letters = []
attempted_letters = []

while game_end == False:
    print(f"You currently have {lives} lives! ")
    guessed_letter = input(" Guess a letter: ").lower()
    
    if guessed_letter in attempted_letters:
        print("You have already attempted this letter")
        print(hangman_art.stages[lives])
        continue
    else:
        attempted_letters += guessed_letter
    
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

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"{guessed_letter} is not in the word! ")
        print("You lost one life! ")
        if lives == 0:
            game_end = True
            print("You lose! ")
            print(f"The word was {chosen_word}!")

    if "_" not in display:
        game_end = True
        print("You Win!")


    print(hangman_art.stages[lives])
    
    

import random
word_list = ["aardvark","baboon","camel"]

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

    if "_" not in display:
        game_end = True
        print("You win!")

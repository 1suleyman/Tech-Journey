import random
word_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for a in chosen_word:
    placeholder += "_ "
print(f"The word contains \n {placeholder} letters\n")


guessed_letter = input(" Guess a letter: ").lower()

display = ""

for letter in chosen_word:
    if letter == guessed_letter:
        display += letter
    else:
        display += "_"
print(f"\n{display}")

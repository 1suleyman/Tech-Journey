import random
word_list = ["aardvark","baboon","camel"]

# 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word, then print it.

chosen_word = random.choice(word_list)
print(chosen_word)

# 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Use the input function to prompt the user and assign the result to guess. Then, convert the guess to lowercase.

guessed_letter = input("Guess a letter: ").lower()
print(guessed_letter)

# 3 - Involves checking if the guessed letter is present in the chosen word. Use a for loop to iterate through each letter in the chosen word and compare it to the guess. Print "Right" if the letter matches the guess, otherwise print "Wrong."

for letter in chosen_word:
    if letter == guessed_letter:
        print("Right")
    else:
        print("Wrong")

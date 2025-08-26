import random

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    max_attempts = 10
elif difficulty == 'hard':
    max_attempts = 5

while attempts < max_attempts:
    guess = input("Make a guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    attempts += 1
    if guess < number_to_guess:
        print("Too low.")
        print(f"You have {max_attempts - attempts} attempts left.")
    elif guess > number_to_guess:
        print("Too high.")
        print(f"You have {max_attempts - attempts} attempts left.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break

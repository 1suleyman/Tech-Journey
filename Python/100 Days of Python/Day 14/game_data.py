# import random module
import random

# import data from game_data.py
from game_data import data

# welcome message
print("Welcome to higher or lower!")
print("Where you have to guess who has more followers on Instagram!")

# function to get a random account from the data
def get_random_account():
    """Get data from random account"""
    return random.choice(data)

# variable to store the first account
account_a = get_random_account()

# score variable
score = 0
# game should continue variable
should_continue = True

while should_continue:
    # get a random account from the data
    account_b = get_random_account()

    # make sure account_a and account_b are not the same
    while account_a == account_b:
        account_b = get_random_account()

    # add a space between rounds
    print("\n" + "-" * 30 + "\n")

    # print the account information
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print("VS")
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # guess validation
    while guess not in ['a', 'b']:
        guess = input("Invalid input. Please type 'A' or 'B': ").lower()

    # get the follower counts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # check if the user is correct
    if (a_follower_count > b_follower_count and guess == 'a') or (b_follower_count > a_follower_count and guess == 'b'):
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        print("\n" + "-" * 30 + "\n")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
        print("\n" + "-" * 30 + "\n")

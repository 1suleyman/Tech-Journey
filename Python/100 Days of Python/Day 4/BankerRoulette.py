# Banker Roulette
import random

print("Welcome to Banker Roulette \n where we get to see who has to pay the bill out of ... ")

friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

print(friends)
random_int = random.randint(0,4)
payer = friends[random_int]
input("Press enter or any key to see who has to pay... ")
print(f"{payer} has to pay!!!")

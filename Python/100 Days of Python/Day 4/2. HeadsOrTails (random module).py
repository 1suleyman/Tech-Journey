import random  

print("Welcome to heads or tails ")
input("Press enter or type anything in to see which you get ")

random_integer = random.randint(1,10)

if (random_integer < 5):
    print("You got HEADS")
else:
    print("You got TAILS")

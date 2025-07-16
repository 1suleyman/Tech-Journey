import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

computer_choice = int(random.randint(0,2))

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. "))
if user_choice >= 0 and user_choice <= 2:
    print(user_choice)
else:
    ("You entered an invalid number")

if (user_choice == 0):
    print(rock)
    if (computer_choice == 0):
        print("Computer chose: ")
        print(computer_choice)
        print(rock)
        print("It's a DRAW!")
    elif (computer_choice == 1):
        print("Computer chose: ")
        print(computer_choice)
        print(paper)
        print("You lose! ")
    else:
        print("Computer chose: ")
        print(computer_choice)
        print(scissors)
        print("You win! ")
elif (user_choice == 1):
    print(paper)
    if (computer_choice == 1):
        print("Computer chose: ")
        print(computer_choice)
        print(paper)
        print("It's a DRAW!")
    elif (computer_choice == 0):
        print("Computer chose: ")
        print(computer_choice)
        print(rock)
        print("You win! ")
    else:
        print("Computer chose: ")
        print(computer_choice)
        print(scissors)
        print("You lose! ")
elif (user_choice == 2):
    print(scissors)
    if (computer_choice == 2):
        print("Computer chose: ")
        print(computer_choice)
        print(scissors)
        print("It's a DRAW!")
    elif (computer_choice == 0):
        print("Computer chose: ")
        print(computer_choice)
        print(rock)
        print("You lose! ")
    else:
        print("Computer chose: ")
        print(computer_choice)
        print(paper)
        print("You win! ")

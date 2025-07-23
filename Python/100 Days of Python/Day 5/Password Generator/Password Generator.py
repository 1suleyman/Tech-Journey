#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# numL = []
# for l in range(1,(nr_letters + 1)):
#     numL.append(l)

# numS = []
# for s in range(1,(nr_symbols + 1)):
#     numS.append(s)

# numN = []
# for n in range(1,(nr_numbers + 1)):
#     numN.append(n)


# final_password = ""

# for l in numL:
#     randomiser_letters = random.randint(0,(int(len(letters))-1))
#     final_password += str(letters[randomiser_letters])

# for l in numS:
#     randomiser_symbols = random.randint(0,(int(len(symbols))-1))
#     final_password += str(symbols[randomiser_symbols])

# for l in numN:
#     randomiser_number = random.randint(0,(int(len(numbers))-1))
#     final_password += str(numbers[randomiser_number])


# print(f"Your password is {final_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

initial_password = []

# Add random letters
for l in range(1,(nr_letters + 1)):
    randomiser_letters = random.randint(0,(int(len(letters))-1))
    initial_password += str(letters[randomiser_letters])

# Add random symbols
for l in range(1,(nr_symbols + 1)):
    randomiser_symbols = random.randint(0,(int(len(symbols))-1))
    initial_password += str(symbols[randomiser_symbols])

# Add random numbers
for l in range(1,(nr_numbers + 1)):
    randomiser_number = random.randint(0,(int(len(numbers))-1))
    initial_password += str(numbers[randomiser_number])

# Shuffle and create the final password
final_password = ''.join(random.sample(initial_password,len(initial_password)))
print(f"Your password is {final_password}")

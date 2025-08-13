alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to the Caesar Cipher Program!")

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    # orginal index before shifting

    original_text_index_places = []
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            original_text_index_places.append(index)
    
    # test confirmation
    # print(f"The current index places are {original_text_index_places} ")

    # new index after shifting
    
    new_index_places = []
    for i in original_text_index_places:
        new_index = (i + shift_amount) % len(alphabet)
        new_index_places.append(new_index)
    
    # test confirmation
    # print(f"The new indexes after being shifted are {new_index_places} ")

    # encrypted message
    
    encrypted_message = ""
    for i in new_index_places:
        encrypted_letter = alphabet[i]
        encrypted_message += encrypted_letter
    
    # test confirmation
    print(f"The encrypted messsage is: {encrypted_message}! ")
    
# encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text,shift_amount):
    # orginal index before shifting
    original_text_index_places = []
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            original_text_index_places.append(index)
    
    # # test confirmation
    # print(f"The current index places are {original_text_index_places} ")

    # new index after shifting
    new_index_places = []
    for i in original_text_index_places:
        new_index = (i - shift_amount) % len(alphabet)
        new_index_places.append(new_index)
    
    # # test confirmation
    # print(f"The new indexes after being shifted back are {new_index_places} ")

    # decrypted message
    
    encrypted_message = ""
    for i in new_index_places:
        encrypted_letter = alphabet[i]
        encrypted_message += encrypted_letter
    
    # test confirmation
    print(f"The decrypted messsage is: {encrypted_message}! ")

def caesar():
    gameover = False
    while gameover == False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if (direction).lower() == "encode":
            encrypt(text,shift)
        
        elif (direction).lower() == "decode":
            decrypt(text,shift)
    
        else:
            print("You entered something wrong, please try again! ")

        choice = input("Would you like to continue yes or no ")
        if choice.lower() == "yes":
            gameover = False
            print("You entered Yes so...")
        elif choice.lower() == "no":
            gameover = True
            print("You entered No so...")
        else:
            print("You entered something wrong, please try again! ")
            gameover = True

caesar()

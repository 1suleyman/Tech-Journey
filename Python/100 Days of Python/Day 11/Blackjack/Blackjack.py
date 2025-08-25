import random

print("Welcome to the game of Blackjack! ")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Jacks, Queens, Kings are worth 10; Aces can be worth 1 or 11

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def play_blackjack():
    game_over = False

    start_playing = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()

    if start_playing == 'no':
        print("Thanks for playing!")
        game_over = True

    if start_playing == 'yes':
        print("Let's play!")
    
    # Initial deal
    initial_player_start = [deal_card(),deal_card()]
    initial_computer_start = [deal_card(),deal_card()]
    player_score = sum(initial_player_start)
    dealer_score = sum(initial_computer_start)
    print(f"Your cards: {initial_player_start}, current score: {player_score}")
    print(f"Dealer's cards are: {initial_computer_start}, current score: {dealer_score}")

    while game_over == False:
        if player_score == 21:
            print("Blackjack! You win!")
            game_over = True
        elif player_score > 21:
            print("You went over 21. You lose!")
            game_over = True
        elif dealer_score == 21:
            print("Dealer has Blackjack! You lose!")
            game_over = True
        elif dealer_score > 21:
            print("Dealer went over 21. You win!")
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                # Deal another card to the player
                new_card = deal_card()
                initial_player_start.append(new_card)
                player_score = sum(initial_player_start)
                print(f"Your cards: {initial_player_start}, current score: {player_score}")
                # dealer's turn
                if dealer_score < player_score and dealer_score < 21:
                    new_dealer_card = deal_card()
                    initial_computer_start.append(new_dealer_card)
                    dealer_score = sum(initial_computer_start)
                    print(f"Dealer's cards: {initial_computer_start}, current score: {dealer_score}")
            else:
                # Dealer's turn
                while dealer_score < player_score and dealer_score < 21:
                    new_dealer_card = deal_card()
                    initial_computer_start.append(new_dealer_card)
                    dealer_score = sum(initial_computer_start)
                    print(f"Dealer's cards: {initial_computer_start}, current score: {dealer_score}")
                game_over = True




play_blackjack()

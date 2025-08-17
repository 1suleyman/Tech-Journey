print("Welcome to the Secret Auction Program!")

game_over = False
bids = {

}

while game_over == False:
    # Get user input for name and bid
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    # Store the bid in the bids dictionary
    bids[name] = bid

    # Ask if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    # Check if the user wants to continue or end the auction
    if should_continue == "no":
        game_over = True
        # Determine the highest bidder
        highest_bidder = ""
        # Initialize highest bid to zero
        highest_bid = 0
        # Loop through the bids to find the highest
        for bidder in bids:
            # If the current bid is higher than the highest bid, update the highest bidder and bid
            if bids[bidder] > highest_bid:
                highest_bidder = bidder
                highest_bid = bids[bidder]
        # Print the winner and their bid
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

    # If there are more bidders, continue the loop
    elif should_continue == "yes":  
        print("Next bidder please!")   
    # If the input is invalid, prompt again
    else:   
        print("Invalid input. Please type 'yes' or 'no'.")
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

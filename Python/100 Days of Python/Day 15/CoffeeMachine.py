MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to the coffee machine!")

shoudl_continue = True

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01


while shoudl_continue:
    # show the user the worth of each american coin that can be used
    print("Here is the worth of each coin you can use:")
    print("Penny: $0.01")
    print("Nickel: $0.05")
    print("Dime: $0.10")
    print("Quarter: $0.25")

    userchoice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # see if you want to turn off the machine by entering "off"
    if userchoice == "off":
        shoudl_continue = False
        print("Turning off the machine. Goodbye!")
        break
    # print a report of all resources
    elif userchoice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        # calculate the total money in the machine by adding up the cost of each drink made
        total_money = 0
        for drink in MENU:
            total_money += MENU[drink]["cost"]
        print(f"Money: ${total_money}")
        continue
    # check if the user choice is valid
    elif userchoice not in MENU:
        print("Invalid choice. Please choose again.")
        continue
    # check if user a chosen a drink in the menu
    elif userchoice == "espresso":
        drink = MENU["espresso"]
    elif userchoice == "latte":
        drink = MENU["latte"]
    elif userchoice == "cappuccino":
        drink = MENU["cappuccino"]
    else:
        print("Invalid choice. Please choose again.")
        continue
    # check if there are enough resources to make the drink

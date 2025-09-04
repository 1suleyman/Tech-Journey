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

should_continue = True

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01

# make totlal money variable outside the loop
total_money = 0

# create a function that deducts the espresso ingredients from the resources
def deduct_espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    # print the water that is left
    print(f"Water left: {resources['water']}ml")
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    # print the coffee that is left
    print(f"Coffee left: {resources['coffee']}g")

# create a function that deducts the latte ingredients from the resources
def deduct_latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    # print the water that is left
    print(f"Water left: {resources['water']}ml")
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    # print the milk that is left
    print(f"Milk left: {resources['milk']}ml")
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    # print the coffee that is left
    print(f"Coffee left: {resources['coffee']}g")

# create a function that deducts the cappuccino ingredients from the resources
def deduct_cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    # print the water that is left
    print(f"Water left: {resources['water']}ml")
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    # print the milk that is left
    print(f"Milk left: {resources['milk']}ml")
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    # print the coffee that is left
    print(f"Coffee left: {resources['coffee']}g")

# check if there are enough resources to make the drink using this function
def check_resources(drink):
    can_make = True
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            can_make = False
        if not can_make:
            continue

# create a function to process coins
def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * quarter_value
    total += int(input("How many dimes?: ")) * dime_value
    total += int(input("How many nickels?: ")) * nickel_value
    total += int(input("How many pennies?: ")) * penny_value
    return total

while should_continue:
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
        # also print the total money earned by the machine
        print(f"The machine currently holds ${total_money}")
        continue
    # check if the user choice is valid
    elif userchoice not in MENU:
        print("Invalid choice. Please choose again.")
        continue
    # check if user a chosen a drink in the menu
    elif userchoice == "espresso":
        drink = MENU["espresso"]
        check_resources(drink)

        # see if the user has inserted enough money to buy the drink
        money_received = process_coins()
        if money_received < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            total_money -= MENU["espresso"]["cost"]
            continue
        elif money_received > drink["cost"]:
            change = round(money_received - drink["cost"], 2)
            print(f"Here is ${change} in change.")
            # add the cost of the drink to the total money
            total_money += MENU["cappuccino"]["cost"]

        # deduct the ingredients from the resources
        deduct_espresso()
    elif userchoice == "latte":
        drink = MENU["latte"]
        check_resources(drink)

        # see if the user has inserted enough money to buy the drink
        money_received = process_coins()
        if money_received < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            total_money -= MENU["espresso"]["cost"]
            continue
        elif money_received > drink["cost"]:
            change = round(money_received - drink["cost"], 2)
            print(f"Here is ${change} in change.")
            # add the cost of the drink to the total money
            total_money += MENU["cappuccino"]["cost"]

        deduct_latte()
    elif userchoice == "cappuccino":
        drink = MENU["cappuccino"]
        check_resources(drink)
        
        # see if the user has inserted enough money to buy the drink
        money_received = process_coins()
        if money_received < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            total_money -= MENU["espresso"]["cost"]
            continue
        elif money_received > drink["cost"]:
            change = round(money_received - drink["cost"], 2)
            print(f"Here is ${change} in change.")
            # add the cost of the drink to the total money
            total_money += MENU["cappuccino"]["cost"]

        deduct_cappuccino()
    else:
        print("Invalid choice. Please choose again.")
        continue

print("Welcome to the calculator app")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    game_over = False
    num1 = float(input("Type your first number: "))

    while game_over == False:
        # shows the options of operations that user can choose
        for symbol in operations:
            print(symbol)
        
        # asks which operator the user wants to choose
        operator = input("Pick a mathmetical operator! ")
        # 
        num2 = float(input("Type your second number: "))


        if operator == "+":
            result = operations["+"](num1, num2)
            print(f"Your answer is: {result}! ")
            num1 = result
        elif operator == "-":
            result = operations["-"](num1, num2)
            print(f"Your answer is: {result}! ")
            num1 = result
        elif operator == "*":
            result = operations["*"](num1, num2)
            print(f"Your answer is: {result}! ")
            num1 = result
        elif operator == "/":
            result = operations["/"](num1, num2)
            print(f"Your answer is: {result}! ")
            num1 = result
        else:
            print("Invalid input. Please choose one of the operators")
            for symbol in operations:
                print(operations[symbol])
            operator = input("Pick a mathmetical operator!")

        # Ask if the user wants to continue
        should_continue = input("Do you want to continue? Type 'yes' or 'no': ").lower()

        # Check if the user wants to continue or end the calculator
        if should_continue == "no":
            game_over = True
            print("Thank you for playing!")

        # If they want to keep playing continue the loop
        elif should_continue == "yes":  
            print("Let's go!")   
        # If the input is invalid, prompt again
        else:   
            print("Invalid input. Please choose one of the operators")
            for symbol in operations:
                print(operations[symbol])
            operator = input("Pick a mathmetical operator!")

calculator()

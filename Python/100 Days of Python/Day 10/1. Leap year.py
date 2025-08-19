print("Welcome to 'Is it a Leap Year'! ")

def is_leap_year(year):
    # Check if the year is divisible by 4.
    # We use the modulo operator (%) to check for a remainder.
    # The "&" operator in Python is a bitwise operator.
    # For conditional logic, you should use the "and" keyword.
    
    if year % 4 == 0:
        # If the year is divisible by 4, we then check the exceptions.
        # This nested if-statement follows the logical rules precisely.
        
        # Check if the year is divisible by 100.
        if year % 100 == 0:
            # If it's divisible by 100, it's NOT a leap year...
            # UNLESS it's also divisible by 400.
            
            # Check if the year is divisible by 400.
            if year % 400 == 0:
                # If it's divisible by 400, it IS a leap year.
                print(f"{year} is a leap year.")
                return True
            else:
                # If it's divisible by 100 but NOT 400, it's NOT a leap year.
                print(f"{year} is not a leap year.")
                return False
        else:
            # If the year is divisible by 4 but NOT by 100, it IS a leap year.
            print(f"{year} is a leap year.")
            return True
    else:
        # If the year is not divisible by 4, it's definitively not a leap year.
        print(f"{year} is not a leap year.")
        return False

is_leap_year(2024)

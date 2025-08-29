# This is how you work out whether if a particular year is a leap year.

# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder

# - unless the year is also divisible by 400 with no remainder

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# turns into 

def is_leap(year):
    if year % 4 == 0:
        print("Divisible by 4")
        if year % 100 == 0:
            print("Divisible by 100")
            if year % 400 == 0:
                print("Divisible by 400")
                return True
            else:
                print("Not divisible by 400")
                return False
        else:
            print("Not divisible by 100")
            return True
    else:
        print("Not divisible by 4")
        return False

print(is_leap(2000))  # Example usage

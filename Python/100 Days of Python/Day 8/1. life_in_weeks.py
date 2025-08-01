print("Welcome to your Life in weeks! ")

user_age = int(input("What is your age? "))

def life_in_weeks(age):
    user_age_in_weeks = age * 52
    x = 4680 - user_age_in_weeks
    print(f"You have {x} weeks left. ")

life_in_weeks(user_age)

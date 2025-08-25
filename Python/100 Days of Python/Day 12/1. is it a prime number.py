print("Welcome to the prime number checker! ")

def is_prime(num):
    # check if num is 1 or less
    if num <= 1:
        return False
    # this checks if num is divisible by any number from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number because it is divisible by {i}.")
            return False
    print(f"{num} is a prime number.")
    return True

is_prime(17)  # Example usage

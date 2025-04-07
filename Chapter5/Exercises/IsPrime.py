#  17. Prime Numbers
#  A prime number is a number that is only evenly divisible by itself and 1. For example, the 
# number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, how
# ever, is not prime because it can be divided evenly by 1, 2, 3, and 6.
#  Write a Boolean function named is_prime which takes an integer as an argument and 
# returns true if the argument is a prime number, or false otherwise. Use the function in 
# a program that prompts the user to enter a number then displays a message indicating 
# whether the number is prime.


def is_prime(number):
    isprime = False
    # Check if the input number is 1.
    # Note: By definition, 1 is not considered a prime number.
    if number == 1:
        isprime = False  # Output "NO" because 1 is not prime.
    else:
        # Loop from 2 to number - 1.
        # This range checks every possible divisor of the number.
        for i in range(2, number):
            # If the number is divisible by i with no remainder,
            # it means the number has a factor other than 1 and itself.
            if number % i == 0:
                isprime = False  # Output "NO" because a divisor was found.
                break  # Exit the loop early since the number is not prime.
            else:
                # This block runs if the for loop completes without finding any factors.
                # It confirms that the number has no divisors other than 1 and itself.
                isprime = True  # Output "YES" because the number is prime.
        return isprime


def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
    
    #return 0
    #return 0


main()
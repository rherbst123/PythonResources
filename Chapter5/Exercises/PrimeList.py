#  18. Prime Number List
#  This exercise assumes that you have already written the is_prime function in Programming 
# Exercise 17. Write another program that displays all of the prime numbers from 1 to 100. 
# The program should have a loop that calls the is_prime function.
import time

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
    size = int(input("Enter range: "))
    number = 0
    start = time.time()
    for number in range(1,size):
        number += 1
    
        if is_prime(number):
            print(f"{number} is prime.")
        #Uncomment below to show unprimes 
        """ 
             else:
             print(f"{number} is not prime.") #
        """
    end = time.time()
    length = end - start
    lengthF = "{:.6f}".format(length)
    print("Calculation time: ", lengthF)
    #return 0
    #return 0


main()
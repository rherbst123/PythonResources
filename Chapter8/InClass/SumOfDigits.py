# 2.  Sum of Digits in a String
# Write a program that asks the user to enter a series of single-digit numbers with nothing 
# separating them. The program should display the sum of all the single digit numbers in the 
# string. For example, if the user enters 2514, the method should return 12, which is the sum 
# of 2, 5, 1, and 4.

def sumOfNumbers(userNumbers):
    numbers = []
    for digit in userNumbers:
        digit = int(digit)
        numbers.append(digit)
    return sum(numbers)

def main():
    userNumbers = input("Enter a bunch of numbers: ")
    print(sumOfNumbers(userNumbers))
main()
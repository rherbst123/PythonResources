""" 12. Maximum of Two Values
 Write a function named max that accepts two integer values as arguments and returns the 
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to 
the function, the function should return 12. Use the function in a program that prompts the 
user to enter two integer values. The program should display the value that is the greater 
of the two. """


def main():
    numA = int(input("Enter a number: "))
    numB = int(input("Enter another number: "))

    isGreaterThan(numA,numB)


def isGreaterThan(numA, numB):
    if numA > numB:
        print(f"{numA} is greater than {numB}")
    if numB > numA:
        print(f"{numB} is greater than {numA}")

main()
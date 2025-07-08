# 2.  Sum of Digits in a String
# Write a program that asks the user to enter a series of single-digit numbers with nothing 
# separating them. The program should display the sum of all the single digit numbers in the 
# string. For example, if the user enters 2514, the method should return 12, which is the sum 
# of 2, 5, 1, and 4



def addition(numbers):
    total = 0
    for ch in numbers:
        #print("\n",ch)
        #Converting each individual "char" into an integer then adding it to itself
        ch = int(ch)
        total += ch
    print(f"The Total is {total}")






def main():
    numbers = input("Smash your keyboard and give me a bunch of numbers ")
    addition(numbers)

main()


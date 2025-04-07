# 20. Random Number Guessing Game
#  Write a program that generates a random number in the range of 1 through 100, and asks 
# the user to guess what the number is. If the user’s guess is higher than the random number, 
# the program should display “Too high, try again.” If the user’s guess is lower than the 
#  random number, the program should display “Too low, try again.” If the user guesses the 
# number, the application should congratulate the user and generate a new random number 
# so the game can start over.

#  Optional Enhancement: Enhance the game so it keeps count of the number of guesses that 
# the user makes. When the user correctly guesses the random number, the program should 
# display the number of guesses.

import random

def numberGen():
    number = random.randint(1,100)
    print(number)
    return number


def guessingGame(number):
    guesses = 0
    guess = int(input("Enter your guess: "))
    while guess != number:
        if guess < number:
            print("Too low, try again.")
            guesses += 1
        else:
            print("Too high, try again.")
            guesses += 1
        guess = int(input("Enter your guess: "))
    print("Congratulations! The guess is correct!")
    print(f"it took you {guesses} guesses")


def main():
    number = numberGen()
    
    guessingGame(number)
    
        
    
main()
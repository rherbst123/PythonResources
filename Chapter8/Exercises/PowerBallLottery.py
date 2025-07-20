# # 13.   PowerBall Lottery
# # To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1–69, 
# # and a “PowerBall” number in the range of 1–26. (You can pick the numbers yourself, or you 
# # can let the ticket machine randomly pick them for you.) Then, on a specified date, a winning 
# # set of numbers is randomly selected by a machine. If your first five numbers match the first 
# # five winning numbers in any order, and your PowerBall number matches the winning Pow-
# # erBall number, then you win the jackpot, which is a very large amount of money. If your 
# # numbers match only some of the winning numbers, you win a lesser amount, depending on 
# # how many of the winning numbers you have matched.
# # 
# In the student sample programs for this book, you will find a file named pbnumbers.txt, 
# # containing  the  winning  PowerBall  numbers  that  were  selected  between  February  3,  2010  
# # and  May  11,  2016  (the  file  contains  654  sets  of  winning  numbers).  Figure  8-6  shows  an  
# # example of the first few lines of the file’s contents. Each line in the file contains the set of six 
# # numbers that were selected on a given date. The numbers are separated by a space, and the 
# # last number in each line is the PowerBall number for that day. For example, the first line in 
# # the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37, 52, and the 
# # PowerBall number 24.


# Write one or more programs that work with this file to perform the following:
# •  Display the 10 most common numbers, ordered by frequency
# •  Display the 10 least common numbers, ordered by frequency
# •  Display  the  10  most  overdue  numbers  (numbers  that  haven’t  been  drawn  in  a  long  
# time), ordered from most overdue to least overdue
# •  Display  the  frequency  of  each  number  1–69,  and  the  frequency  of  each  Powerball  
# number 1–26

import random as r

def pickLine(lines):
    winningNumbers = []
    line_number = r.randint(1,654)
    winningLine = lines[line_number - 1].strip()
    for number in winningLine.split():
        winningNumbers.append(int(number))
    #print(winningNumbers)
    return winningNumbers
    
def getGuess(winning_numbers):
    user_guess = []
    manualOrBot = input("Do you want to draw random numbers or choose your own? (random/choose): ")
    if manualOrBot == "random":
        
        for counter in range(5):
            randomNumber = r.randint(1,70)
            user_guess.append(randomNumber)
            counter += 1
        user_guess.append(r.randint(1,26))

        #print(user_guess)
        #print("Winning Numbers: ",winning_numbers)
    

    if manualOrBot == "choose":
        for counter in range(5):
            number = int(input("Guess a Number from 1-69: "))
            while number < 1 or number > 69:
                print("Invalid input. Please enter a number between 1 and 69.")
                number = int(input("Guess a Number from 1-69: "))
            user_guess.append(number)
        number = int(input("Enter the POWER number 1-26: "))
        while number < 1 or number > 26:
            print("Too high")
            number = int(input("Enter the POWER number 1-26: "))
        user_guess.append(number)
    isWinning(user_guess, winning_numbers)
    return user_guess

def isWinning(user_guess, winning_numbers):
    prises = 0
    if user_guess == winning_numbers:
        print("HOLY SHIT YOU WON EVERYTHING")
    if user_guess[0] in winning_numbers:
        print(f"Your first number is in the set!: {user_guess[0]}, you win 100")
        prises += 1
    if user_guess[1] in winning_numbers:
        print(f"Your Second number is in the set!: {user_guess[0]}, you win 100")
        prises += 1
    if user_guess[2] in winning_numbers:
        print(f"Your Third number is in the set!: {user_guess[0]}, you win 100")
        prises += 1
    if user_guess[3] in winning_numbers:
        print(f"Your Fourth number is in the set!: {user_guess[0]}, you win 100")
        prises += 1
    if user_guess[4] in winning_numbers:
        print(f"Your POWERBALL number is in the set!: {user_guess[0]}, you win 100")
        prises += 1
    
    if prises == 0:
        print("Sorry Pal you lost")
    if prises > 0:
        print(f"You have won: ${prises}00!!!")

    print(f"Here are the winning numbers: {winning_numbers}")    

def greatestNumbers(lines):
    foundLargest = []
    for _ in range(10):
        largest_number = 0
        for line in lines:
            for numbers in line.split():
                number = int(numbers)
                if number > largest_number and number not in foundLargest:
                    largest_number = number
        foundLargest.append(largest_number)
    
    return foundLargest


def smallestNumbers(lines):
    foundSmalls = []
    for _ in range(10):
        smallest_number = 70
        for line in lines:
            for numbers in line.split():
                number = int(numbers)
                if number < smallest_number and number not in foundSmalls:
                    smallest_number = number
        foundSmalls.append(smallest_number)
    return foundSmalls
    
#def findOverdue(lines):

        



def main():
    with open(r"Chapter8/Files/pbnumbers.txt",'r') as file:
        lines = file.readlines()
    winning_numbers = pickLine(lines)
    #print(f"The Winning Numbers are: {winningNumbers}")

    print("Welecome to the lottery!")
    user_guess = getGuess(winning_numbers)
    print(f"Users Ticket: {user_guess}")
    greatestNumbers(lines)
    smallestNumbers(lines)


    
            
            


main()
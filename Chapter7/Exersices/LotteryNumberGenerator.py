#  2. Lottery Number Generator
#  VideoNote
#  The Lottery Number 
# Generator Problem
#  Design a program that generates a seven-digit lottery number. The program should gener
# ate seven random numbers, each in the range of 0 through 9, and assign each number to a 
# list element. (Random numbers were discussed in Chapter 5.) Then write another loop that 
# displays the contents of the list

import random

lotteryNumber = []

for i in range(7):
    randomNum = random.randint(0,9)
    lotteryNumber.append(randomNum)

# Print the lottery numbers as a single whole number
print("Your Lottery number is... ")

#join each entry in the list one by one
print(''.join(str(num) for num in lotteryNumber))

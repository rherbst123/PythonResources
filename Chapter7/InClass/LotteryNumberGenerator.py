# 2.  Lottery Number Generator
# Design a program that generates a seven-digit lottery number. The program should gener-
# ate seven random numbers, each in the range of 0 through 9, and assign each number to a 
# list element. (Random numbers were discussed in Chapter 5.) Then write another loop that 
# displays the contents of the list.

import random

#Empty List that will be our lottery number
lottery_Number = []

for i in range(7):
    randomDigit = random.randint(0,9)
    lottery_Number.append(randomDigit)

print("Here is your lottery number....")
#print("\n")
for digit in lottery_Number:
    print(digit, end="")
print("\n")

print(''.join(str(num) for num in lottery_Number))
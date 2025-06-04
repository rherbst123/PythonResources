# 6.  Dice Rolling Function 
# In  a  program,  write  a  function  named  roll  that  accepts  an  integer  argument  number_
# of_throws. The function should  generate and  return a  sorted list  of  number_of_throws 
# random numbers between 1 and 6. The program should prompt the user to enter a positive 
# integer that is sent to the function, and then print the returned list.

import random

def roll(number_of_throws):
    print(number_of_throws)
    throws = []
    for counter in range(number_of_throws):
        dice = random.randint(1,6)
        throws.append(dice)
    throws.sort()
    print(throws)
    
    

def main():
    number_of_throws = int(input("How many throws to throw?: "))
    roll(number_of_throws)
    

main()
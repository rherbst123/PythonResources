# 21. Rock, Paper, Scissors Game
#  Write a program that lets the user play the game of Rock, Paper, Scissors against the com
# puter. The program should work as follows:
#  1.  When the program begins, a random number in the range of 1 through 3 is generated. 
# If the number is 1, then the computer has chosen rock. If the number is 2, then the 
# computer has chosen paper. If the number is 3, then the computer has chosen scissors. 
# (Don’t display the computer’s choice yet.)
#  2.  The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
#  3. The computer’s choice is displayed.
#  4.  A winner is selected according to the following rules:
#  •	If	one	player	chooses	rock	and	the	other	player	chooses	scissors,	then	rock	wins.	 
# (Rock smashes scissors.)
#  •	If	one	player	chooses	scissors	and	the	other	player	chooses	paper,	then	scissors	wins.	
# (Scissors cuts paper.)
#  •	If	one	player	chooses	paper	and	the	other	player	chooses	rock,	then	paper	wins.	
# (Paper wraps rock.)
#  •	If	both	players	make	the	same	choice,	the	game	must	be	played	again	to	determine	
# the winner.

import random


def machineGuess():
    machine = random.randint(1,3)
    #print(machine) #See machines choice
    return machine


def rps(machine, user):
    # Print machine's choice using if statements
    if machine == 1:
        print("Machine chose: rock")
    elif machine == 2:
        print("Machine chose: paper")
    elif machine == 3:
        print("Machine chose: scissors")
    
    # Determine and print the winner using only if statements
    if machine == user:
        print("It's a draw! Play again.")
    elif user == 1:
        if machine == 3:
            print("User wins!")
        else:
            print("Machine wins!")
    elif user == 2:
        if machine == 1:
            print("User wins!")
        else:
            print("Machine wins!")
    elif user == 3:
        if machine == 2:
            print("User wins!")
        else:
            print("Machine wins!")
    
    

def main():
    machine = machineGuess()
    user = int(input("Enter your choice Rock Paper Scissors: 1=Rock, 2=Paper, 3=Scissors "))
    rps(machine, user)

main()




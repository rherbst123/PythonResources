"""  10. Money Counting Game
 Create a change-counting game that gets the user to enter the number of coins required 
to make exactly one dollar. The program should prompt the user to enter the number of 
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one 
dollar, the program should congratulate the user for winning the game. Otherwise, the 
program should display a message indicating whether the amount entered was more than 
or less than one dollar """

#amnounts of each denomination 
pennies = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
dollar = 1.00


numPennies = int(input("Enter how many pennies you want to put on the table: "))
numPennies = numPennies * 0.01

numNickel = int(input("Enter how many nickels you want to put on the table: "))
numNickel = numNickel * 0.05

numDime = int(input("Enter how many dimes you want to put on the table: "))
numDime = numDime * 0.10

numQuarter = int(input("Enter how many quarters you want to put on the table: "))
numQuarter = numQuarter * 0.25

total = numQuarter +  numDime + numNickel + numPennies
total = float(total)
print("You entered a total amount of: ", total)

if total == dollar:
    print("You won!")
elif total > dollar:
    print("Too High!")
elif total < dollar:
    print("To Low!")
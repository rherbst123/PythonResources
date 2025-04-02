#  8. Paint Job Estimator
#  A painting company has determined that for every 112 square feet of wall space, one gallon 
# of paint and eight hours of labor will be required. The company charges $35.00 per hour 
# for labor. Write a program that asks the user to enter the square feet of wall space to be 
# painted and the price of the paint per gallon. The program should display the following data:
#  • The number of gallons of paint required
#  • The hours of labor required
#  • The cost of the paint
#  • The labor charges
#  • The total cost of the paint job




def totalCost(wallSpace):
    rate = wallSpace / 112
    hoursNeeded = rate * 8
    
    return rate, hoursNeeded


wallSpace = int(input("How much wall space needs to be painted?: "))
pricePerGal = int(input("How much does a gallon of paint cost?: "))

print(totalCost(wallSpace, hoursNeeded))


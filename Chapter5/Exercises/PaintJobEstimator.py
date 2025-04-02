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




def totalCost(wallSpace, pricePerGal):
    numOfPaintReq = wallSpace // 112   #EX 112sq Feet of wall space for one gallon
    hoursNeeded = (wallSpace // 112) * 8 # go off of paint cans, need 8 hours PER can
    ratePerHour = hoursNeeded * 35
    priceForPaint = numOfPaintReq * pricePerGal

    finalCost = ratePerHour + priceForPaint

    
    return numOfPaintReq , hoursNeeded , ratePerHour , pricePerGal, finalCost


wallSpace = int(input("How much wall space needs to be painted?: "))
pricePerGal = int(input("How much does a gallon of paint cost?: "))


numofPaintReq, hoursNeeded , ratePerHour, pricePerGal, finalCost = totalCost(wallSpace, pricePerGal)

print(f"The number of paint cans needed for the job: {numofPaintReq}")
print(f"The amount of man hours needed: {hoursNeeded}")
print(f"The total cost of labor is: ${ratePerHour}")
print(f"The cost of each gallon used is: ${pricePerGal}")
print(f"All these costs come out to a total of: ${finalCost}")


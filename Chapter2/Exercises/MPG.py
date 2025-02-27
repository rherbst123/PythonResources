"""  A car's miles-per-gallon (MPG) can be calculated with the following formula:
 MPG 5 Miles driven 4 Gallons of gas used
 Write a program that asks the user for the number of miles driven and the gallons of gas 
used. It should calculate the car's MPG and display the result

 """


galUsage = float(input("Enter the amount of gallons used: "))



distanceDriven = float(input("Enter the amount of miles driven: "))

mpg = (distanceDriven / galUsage)
float(mpg)

print("The car gets", mpg, "miles per gallon")
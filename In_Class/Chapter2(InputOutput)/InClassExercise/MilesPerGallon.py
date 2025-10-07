# 7.  Miles-per-Gallon
# A car's miles-per-gallon (MPG) can be calculated with the following formula:
# MPG 5 Miles driven 4 Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas 
# used. It should calculate the car's MPG and display the result.


milesDriven = float(input("How many miles have you driven?: "))

gallonsUsed = float(input("How many gallons used on this drive?: "))

Mpg = milesDriven / gallonsUsed

print(f"You drove: {milesDriven}, and used {gallonsUsed} gallons. Which means your car has a MPG of: {format(Mpg, "0.2f")}")

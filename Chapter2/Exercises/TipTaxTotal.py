""" Write a program that calculates the total amount of a meal purchased at a restaurant. The 
program should ask the user to enter the charge for the food, then calculate the amounts 
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total. """

billAmount = float(input("How much was the bill?: "))

salesTax = (0.07 * billAmount)

tip = (0.18 * billAmount)

print("Sales tax:", format(salesTax, "0.2f"), "tip:", format(tip, "0.2f"))

finalTotal = (billAmount + salesTax + tip)
print("Your final total will be:", format(finalTotal, '0.2f'))

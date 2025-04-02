"""  3. How Much Insurance?
 Many financial experts advise that property owners should insure their homes or buildings 
for at least 80 percent of the amount it would cost to replace the structure. Write a program 
that asks the user to enter the replacement cost of a building, then displays the minimum 
amount of insurance he or she should buy for the property. """


def costToReplace(costOfHouse):
    repCost = costOfHouse * 0.80
    repCost = format(repCost,"0.2f")
    return repCost

costOfHouse = float(input("Enter how much your house costs: "))

print(costToReplace(costOfHouse))
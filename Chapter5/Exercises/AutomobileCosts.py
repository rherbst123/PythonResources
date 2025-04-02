"""  4. Automobile Costs
 Write a program that asks the user to enter the monthly costs for the following expenses 
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and 
maintenance. The program should then display the total monthly cost of these expenses, 
and the total annual cost of these expenses. """

expenses = ["loan payment", "insurance", "gas", "oil", "tires", "maintenance"]

costs = []
expense = 0
for counter in range(6):
    
    expenseCost = int(input(f"Enter the cost for {expenses[expense]}: "))
    expense += 1
    costs.append(expenseCost)
#print(costs)

def monthlyCost(costs):
    return sum(costs)

def yearlyCost(costs):
    yearly = sum(costs) * 12
    return yearly

print(f"Total monthly cost: ${monthlyCost(costs)}") #make sure to use print(f"sdasassadsa")
print(f"Total annual cost: ${yearlyCost(costs)}")
# 14.  Expense Pie Chart
# Create a text file that contains your expenses for last month in the following categories:
# •  Rent
# •  Gas
# •  Food
# •  Clothing
# •  Car payment
# •  Misc
# Write a Python program that reads the data from the file and uses matplotlib to plot a pie 
# chart showing how you spend your money.

import matplotlib.pyplot as plt

# Rent: 750
# Gas: 25
# Food: 450
# Clothing: 10
# Car payment: 10
# Misc: 50

# Read data
categories = ["Rent","Gas","Food","Clothing","Car Payment", "Misc"]
amounts = [750,25,450,10,10,50]
# with open('C:\\Users\\riley\\Documents\\GitHub\\PythonResources\\Chapter7\\Extra_Files\\Expenses.txt', 'r') as file:
#     for line in file:
#         #Rent, Amount eg 750
#         category, amount = line.strip().split(':')
#         categories.append(category.strip())
#         amounts.append(float(amount.strip()))

# Plot pie chart
plt.pie(amounts, labels=categories)
plt.title('Monthly Expenses')
plt.show()

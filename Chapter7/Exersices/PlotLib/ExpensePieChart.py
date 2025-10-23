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

# Read data
categories = []
amounts = []
with open('C:\\Users\\riley\\Documents\\GitHub\\PythonResources\\Chapter7\\Extra_Files\\Expenses.txt', 'r') as file:
    for line in file:
        category, amount = line.strip().split(':')
        categories.append(category.strip())
        amounts.append(float(amount.strip()))

# Plot pie chart
plt.pie(amounts, labels=categories, autopct='%1.1f%%')
plt.title('Monthly Expenses')
plt.show()

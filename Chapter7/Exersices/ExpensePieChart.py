# 4.  Expense Pie Chart
# Create a text file that contains your expenses for last month in the following categories:
# •  Rent
# •  Gas
# •  Food
# •  Clothing
# •  Car payment
# •  Misc
# Write a Python program that reads the data from the file and uses matplotlib to plot a pie 
# chart showing how you spend your money

import matplotlib.pyplot as plt


file = open("Chapter7/Extra_Files/Expenses.txt", 'r')
expenses = []
prices = []

for line in file:
    colon_index = line.find(':')
    
    expense = line[:colon_index].strip()
    expenses.append(expense)
    
    price = float(line[colon_index + 1:].strip())
    prices.append(price)
    #print(f"Expense: {expense}, Price: {price}")

file.close()
#print(expenses, prices)


fig, ax = plt.subplots()

ax.pie(prices, labels=expenses)
plt.show()

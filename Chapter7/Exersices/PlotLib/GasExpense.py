# 15.  1994 Weekly Gas Graph
# In the student sample programs for this book, you will find a text file named 1994_Weekly_
# Gas_Averages.txt. The file contains the average gas price for each week in the year 1994. 
# (There are 52 lines in the file.) Using matplotlib, write a Python program that reads the 
# contents of the file then plots the data as either a line graph or a bar chart. Be sure to display 
# meaningful labels along the X and Y axes, as well as the tick marks.

import matplotlib.pyplot as plt

# Read the gas prices from the file
gas_prices = []
with open('C:\\Users\\riley\\Documents\\GitHub\\PythonResources\\Chapter7\\Extra_Files\\GasExpense.txt', 'r') as file:
    for line in file:
        gas_prices.append(float(line.strip()))

# Create week numbers (1-52)
weeks = list(range(1, len(gas_prices) + 1))

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(weeks, gas_prices, marker='o', linewidth=2, markersize=4)

# Add labels and title
plt.xlabel('Week Number', fontsize=12)
plt.ylabel('Average Gas Price ($)', fontsize=12)
plt.title('1994 Weekly Gas Averages', fontsize=14, fontweight='bold')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
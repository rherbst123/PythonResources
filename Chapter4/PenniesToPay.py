#  7. Pennies for Pay
#  Write a program that calculates the amount of money a person would earn over a period of 
# time if his or her salary is one penny the first day, two pennies the second day, and contin
# ues to double each day. The program should ask the user for the number of days. Display 
# a table showing what the salary was for each day, then show the total pay at the end of the 
# period. The output should be displayed in a dollar amount, not the number of pennies.


days = int(input("How many days?: "))
start = 0.01

for i in range(days):
    #print(start)
    start = start * 2
print("Final pay", start)
# 2.  Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write 
# a program that asks the user to enter the projected amount of total sales, then displays the 
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.


total_Sales = int(input("What is the predicted total sales?: "))


profit = total_Sales * 0.23

#print("$",profit)

print(f"${profit}")
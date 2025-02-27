""" Write a program that asks the user to enter the amount of a purchase and the desired 
number of payment instalments. The program should add 5 percent to the amount to get 
the total purchase amount, and then divide it by the desired number of instalments, then 
 display messages telling the user the total amount of the purchase and how much each  """

itemPrice = float(input("Enter the price of your Item: "))

paymentNum = int(input("Enter the amound of payments for this item: "))

print("Your item costs:", itemPrice,", And you would like to pay it off in", paymentNum, "payment's")
payment = float(paymentNum)

paymentAmount = (itemPrice / paymentNum)
print("Each payment will be:", format(paymentAmount, "0.2f"))

intrest = 0.05
intrest = paymentAmount * intrest
format(intrest, "0.2f")
print("Intrest for each payment:", format(intrest, "0.2f"))

payment = (paymentAmount + intrest)

print("So each payment will be", format(payment, "0.2f"))





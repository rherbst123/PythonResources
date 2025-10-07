# 6.  Payment Instalments
# Write  a  program  that  asks  the  user  to  enter  the  amount  of  a  purchase  and  the  desired  
# number of payment instalments. The program should add 5 percent to the amount to get 
# the total purchase amount, and then divide it by the desired number of instalments, then 
# The Sales 
# Prediction Problem
# display  messages  telling  the  user  the  total  amount  of  the  purchase  and  how  much  each  
# instalment will cost.


TAX = 0.05

purchaceAmount = float(input("What is the purchace amount?: "))

installmentAmount = int(input("How many installments?: "))
installmentAmount = float(installmentAmount)

intrest = purchaceAmount * TAX


totalAmount = purchaceAmount + intrest

print(totalAmount)

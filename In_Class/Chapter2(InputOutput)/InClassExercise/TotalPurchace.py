# 4.  Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of 
# each  item,  then  displays  the  subtotal  of  the  sale,  the  amount  of  sales  tax,  and  the  total.  
# Assume the sales tax is 7 percent.

SALES_TAX = 0.07

item1 = float(input("What is the price of item1: "))
item2 = float(input("What is the price of item2: "))
item3 = float(input("What is the price of item3: "))
item4 = float(input("What is the price of item4: "))
item5 = float(input("What is the price of item5: "))

subTotal = item1 + item2 + item3 + item4 + item5

salesTax = subTotal * SALES_TAX

wholeTotal = subTotal + salesTax

print(f"Your SubTotal is: ${subTotal}")

print(f"Your salesTax is: ${format(salesTax, "0.2f")}")

print(f"Your Grand Total is: ${format(wholeTotal, "0.2f")}")
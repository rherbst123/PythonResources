""" A customer in a store is purchasing five items. Write a program that asks for the price of 
each item, then displays the subtotal of the sale, the amount of sales tax, and the total. 
Assume the sales tax is 7 percent """


item1 = input("Enter price for item 1:")
item2 = input("Enter price for item 2:")
item3 = input("Enter price for item 3:")
item4 = input("Enter price for item 4:")
item5 = input("Enter price for item 5:")

item1 = float(item1)
item2 = float(item2)
item3 = float(item3)
item4 = float(item4)
item5 = float(item5)

print("Here are itemised prices:" "\n", item1, "\n",item2, "\n" , item3, "\n", item4, "\n", item5)

subtotal = item1 + item2 + item3 + item4 + item5
#float(subtotal)
format(subtotal, ".2f")


print("Here is subtotal, without tax:", subtotal)

tax = 0.07
Total = subtotal * tax
format(Total, ".2f")
print("Tax is:", Total)


finalTotal = Total + subtotal
format(finalTotal, ".2f")
print("Final price:", finalTotal)


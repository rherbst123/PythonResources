#  12. Software Sales
#  A software company sells a package that retails for $99. Quantity discounts are given 
# according to the following table:
#  Quantity
#  Discount
#  10–19: 10 %
#  20–49: 20%
#  50–99: 30%
#  100 or more:  40%

#  Write a program that asks the user to enter the number of packages purchased. The pro
# gram should then display the amount of the discount (if any) and the total amount of the 
# purchase after the discount.

PACKAGE_PRICE = 99.00

quantity = int(input("Enter the amount of packages purchced: "))

totalAmount = PACKAGE_PRICE * quantity
print("Your total amount spent is: ", totalAmount)

if quantity > 9 or quantity < 20:
    discount = totalAmount * 0.10

if quantity > 20 or quantity < 50:
    discount = totalAmount * 0.20
    
if quantity > 49 or quantity < 100:
    discount = totalAmount * 0.30

if quantity > 100:
    discount = totalAmount * 0.40

totalWDiscount = totalAmount - discount
print("You have bought: ", quantity, "Packages.", discount, "is your discount which brings you to a toal of: ", totalWDiscount )
# 13. Shipping Charges
#  The Fast Freight Shipping Company charges the following rates:
#  Weight of Package
#  Rate per Pound
#  2 pounds or less $1.50
#  Over 2 pounds but not more than 6 pounds: $3.00
#  Over 6 pounds but not more than 10 pounds: $4.00
#  Over 10 pounds: 4.75
#  Write a program that asks the user to enter the weight of a package then displays the shipping charges

weightOfPackage = float(input("Enter the weight of your package: "))

rate = 1.00
if weightOfPackage < 2:
    rate = 1.50
if weightOfPackage > 2 and weightOfPackage < 7:
    rate = 3.00
if weightOfPackage > 6 and weightOfPackage < 11:
    rate = 4.00
if weightOfPackage > 10:
    rate = 4.75

finalPrice = weightOfPackage * rate


print("The final price is: ", finalPrice)



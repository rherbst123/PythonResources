"""  Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the 
purchase:
 • The number of shares that Joe purchased was 2,000.
 • When Joe purchased the stock, he paid $40.00 per share.
 • Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid 
for the stock.
 Two weeks later, Joe sold the stock. Here are the details of the sale:
 • The number of shares that Joe sold was 2,000.
 • He sold the stock for $42.75 per share.
 • He paid his stockbroker another commission that amounted to 3 percent of the amount 
he received for the stock.
 Write a program that displays the following information:
 • The amount of money Joe paid for the stock.
 • The amount of commission Joe paid his broker when he bought the stock.
 • The amount for which Joe sold the stock.
 • The amount of commission Joe paid his broker when he sold the stock.
 • Display the amount of money that Joe had left when he sold the stock and paid his 
broker (both times). If this amount is positive, then Joe made a profit. If the amount is 
negative, then Joe lost money """
numberOfStocks = 2000.00
stockPrice = 40.00
comission = 0.03

comissionTotal = (stockPrice * comission)


newPrice = 42.75
soldTotal = newPrice * numberOfStocks
soldComission = soldTotal * comission



print("Joe paid:", stockPrice, "Dollars for each stock.", 
      "He paid","$",comissionTotal, "in comission"
     )

print("When he sold his stock he sold it for a total of:", soldTotal,
      "With a comission of:", soldComission)

print("After comission Joe had a total of:", soldTotal - soldComission - comissionTotal)



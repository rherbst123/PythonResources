"""  9. Monthly Sales Tax
 A retail company must file a monthly sales tax report listing the total sales for the month, 
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent 
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter 
the total sales for the month. From this figure, the application should calculate and display 
the following:
 • The amount of county sales tax
 • The amount of state sales tax
 • The total sales tax (county plus state) """


def main():
    totalSales = float(input("What is the montly earning?: $"))
    countyTax = countySalesTax(totalSales)  # make sure you specify that you are saying what each one is
    stateTax = stateSalesTax(totalSales)
    totalTax = totalSalesTax(countyTax, stateTax)

    print(f"The county tax is: ${countyTax:.2f}")
    print(f"The state tax is: ${stateTax:.2f}")
    print(f"Total tax is: ${totalTax:.2f}")

    return 0


def countySalesTax(totalSales):
    countyTax = totalSales * 0.025
    return countyTax


def stateSalesTax(totalSales):
    stateTax = totalSales * 0.05
    return stateTax

def totalSalesTax(countyTax, stateTax):
    totalTax = countyTax + stateTax
    return totalTax


main()






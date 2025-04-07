#  19. Loan Payments Calculator
#  Suppose you have taken out a loan for a certain amount of money with a fixed monthly inter
# est rate and monthly payments, and you want to determine the monthly payment amount 
# necessary to pay off the loan within a specific number of months. The formula is as follows:
#         
# 
#   p = (R * A) / (1 - (1 + R)**-M)
# 
# 
# The terms in the formula are:
#  •	P is the payment amount per month.
#  •	R is the monthly interest rate, as a decimal (e.g. 2.5% 5 0.025).
#  •	A is the amount of the loan.
#  •	M is the number of months.
#  Write a program that prompts the user to enter the loan amount, monthly interest rate as 
# a percentage and desired number of months. The program should pass these values to a 
# function that reeturns the monthly payment amount necessary. The program should display this amount


def loanCalc(loan,interest,months):
    p = (interest * loan) / (1.0- (1.0 + interest)**-months)
    return p

def main():
    loan = float(input("What is your loan amount?: "))
    interest = float(input("What percentage interest?: %"))
    interest = float(interest/100.0)
    #print(interest)
    months = float(input("For how many months?: "))
    
    p = loanCalc(loan,interest,months)
    p = format(p,"0.2f")
    print(f"Your monthly payment will be: ${p}")
main()
    
    
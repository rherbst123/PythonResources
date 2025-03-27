""" # 16. February Days
#  The month of February normally has 28 days. But if it is a leap year, February has 29 days. 
# Write a program that asks the user to enter a year. The program should then display the 
# number of days in February that year. Use the following criteria to identify leap years:
#  1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only 
# if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
#  2. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4. 
# For example, 2008 is a leap year, but 2009 is not.
#  Here is a sample run of the program:
#  Enter a year: 2008 Enter
#  In 2008 February has 29 days

 """

year = int(input("Enter a year: "))

def leapYear(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 4 == 0 and year % 100 ==0:
            leap = False
            if year % 4 == 0 and year % 100 ==0 and year % 400 == 0:
                leap = True
    return leap

print(leapYear(year))


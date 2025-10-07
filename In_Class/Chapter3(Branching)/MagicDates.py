# 6.  Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the 
# month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two-
# digit year. The program should then determine whether the month times the day equals the 
# year. If so, it should display a message saying the date is magic. Otherwise, it should display 
# a message saying the date is not magic.

day = int(input("Enter a day: 1-31: "))
month = int(input("Enter a month: 1-12: "))
year = int(input("Enter the last 2 digits of the year: 1 - 99: "))

magicNumber = day * month

if magicNumber == year:
    print(f"We have a magic Number: {magicNumber} with the year {year}")
else:
    print(f"Here is the date entered: {day}/{month}/{year}")



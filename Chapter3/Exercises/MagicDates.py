"""  The date June 10, 1960, is special because when it is written in the following format, the 
month times the day equals the year:
 6/10/60
 Design a program that asks the user to enter a month (in numeric form), a day, and a two
digit year. The program should then determine whether the month times the day equals the 
year. If so, it should display a message saying the date is magic. Otherwise, it should display 
a message saying the date is not magic """

day = input("Enter the day: EX:1-31: ")

month = input("Enter the month: EX: 1-12: ")

year = input("Enter 2 digit year: EX 1-99: ")

#fullDate = day + month + year
print("Full date: ", day,"/",month,"/",year)
day = int(day)
month = int(month)
year = int(year)


magicNumber = day * month
print("The Magic number is... ",magicNumber)

if magicNumber == year:
    print("horray magic number found! ", magicNumber, "is equal to ", year)
# 8.  Name Search
# If you have downloaded the source code you will find the following files in the Chapter 07 
# folder:
# •  GirlNames.txt  This  file  contains  a  list  of  the  200  most  popular  names  given  to  girls  
# born in the United States from the year 2000 through 2009.
# •  BoyNames.txt  This  file  contains  a  list  of  the  200  most  popular  names  given  to  boys  
# born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate lists. The user 
# should be able to enter a boy’s name, a girl’s name, or both, and the application will display 
# messages indicating whether the names were among the most popular.


with open('/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/GirlNames.txt', 'r') as file:
    Girl_names = [line.strip() for line in file if line.strip()]


with open('/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/BoyNames.txt', 'r') as file:
    Boy_names = [line.strip() for line in file if line.strip()]


name = input("Enter a name you want to see if it is popular: ")


if name in Girl_names:
    print(f"{name} is in the girl names")
else:
    print("Not in the Girls list")


if name in Boy_names:
    print(f"{name} is in boy names")
else:
    print("Not in Boys list")
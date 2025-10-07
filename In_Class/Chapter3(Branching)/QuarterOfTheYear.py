# 3.  Quarter of the Year
# Write  a  program  that  asks  the  user  for  a  month  as  a  number  between  1  and  12.  The  
# program  should  display  a  message  indicating  whether  the  month  is  in  the  first  quarter,  
# the second quarter, the third quarter, or the fourth quarter of the year. Following are the 
# guidelines:
# •  If the user enters either 1, 2, or 3, the month is in the first quarter.
# •  If the user enters a number between 4 and 6, the month is in the second quarter.
# •  If the number is either 7, 8, or 9, the month is in the third quarter.
# •  If the month is between 10 and 12, the month is in the fourth quarter.
# •  If the number is not between 1 and 12, the program should display an error.

#Enter the month
month = int(input("Enter a number corresponding to a Month 1-12: "))


if month == 1 or month == 2 or month == 3:
    print("The month is in the first quarter")
if month == 4 or month == 5 or month == 6:
    print("The month is in the second quarter")
if month == 7 or month == 8 or month == 9:
    print("The month is in the third quarter")
if month == 10  or month == 11 or month == 12:
    print("The month is in the fourth quarter")
if month > 12 or month < 1:
    print("Error")
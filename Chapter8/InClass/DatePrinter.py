# 3.  Date Printer
# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. 
# It should print the date in the format March 12, 2018


def convertDate(date):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # month = months[(int(date[0:2]) -1)]
    # day = int(date[3:5])
    # year = int(date[6:10])
    # print(month, day, year)

    month, day, year = date.split("/")
    print(month, day, year)
    
def main():
    date = input("Enter a date in the following format mm/dd/yyyy: ")
    convertDate(date)

main()
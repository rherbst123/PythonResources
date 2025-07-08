# 3.  Date Printer
# Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. 
# It should print the date in the format March 12, 2018.



def conversion(date):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    

    month = months[(int(date[0:2]) - 1)]
    day = int(date[4:5])
    year = int(date[6:11])
    print(f"The formatted date is {month} {day}, {year} ")


def main():
    date = input("Enter a date in the mm/dd/yyyy format: ")
    conversion(date)

main()
# 5.  Charge Account Validation
# If you have downloaded the source code from the Premium Companion Website you will 
# find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a 
# company’s  valid  charge  account  numbers.  Each  account  number  is  a  seven-digit  number,  
# such as 5658845.
# Write  a  program  that  reads  the  contents  of  the  file  into  a  list.  The  program  should  then  
# ask  the  user  to  enter  a  charge  account  number.  The  program  should  determine  whether   
# the number is valid by searching for it in the list. If the number is in the list, the program 
# should display a message indicating the number is valid. If the number is not in the list, the 
# program should display a message indicating the number is invalid

# Open the file, read each valid account and store them in a list
with open('/home/riley/Documents/GitHub/RileyPython/Chapter7/Extra_Files/charge_accounts.txt', 'r') as file:
    valid_accounts = [line.strip() for line in file if line.strip()]

print(valid_accounts)

# Ask user for a charge account number
account_number = input("Enter a charge account number: ")

# Check if the entered account number is valid
if account_number in valid_accounts:
    print("The charge account number is valid.")
else:
    print("The charge account number is invalid.")
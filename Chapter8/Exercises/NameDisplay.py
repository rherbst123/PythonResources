# 1.  Name Display
# Write  a  program  that  gets  strings  containing  a  person’s  first  and  last  name  as  separate  
# values,  and  then  displays  their  “initials”,  “name  in  address  book”,  and  “username”.  For  
# example, if the user enters a first name of “John” and a last name of “Smith”, the program 
# should display “J.S.”, “John SMITH”, and “jsmith


def get_names():
    first_name = input("Please Enter your First name: ")
    last_name = input("Please Enter your Last name: ")
    names(first_name, last_name)
    



def names(first_name, last_name):
    # take the first element of the first and last name. Seperate them by a period and end it with
    Initials = first_name[0].upper()+"."+ last_name[0].upper()+"."
    print(f"Your Initials are: {Initials}")
    # Take the first name and leave it, Convert last name to full caps
    address_book = first_name +" "+ last_name.upper()
    print(f"Your Name in peoples addresses books is: {address_book}") 
    #Take the first name element and lower it. Lowercase the full last name   
    userName = first_name[0].lower()+ last_name.lower()
    print(f"Your name on xbox is: {userName}")


def main():
    get_names()

main()
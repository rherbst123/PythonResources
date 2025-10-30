# 1.  Name Display
# Write  a  program  that  gets  strings  containing  a  person’s  first  and  last  name  as  separate  
# values,  and  then  displays  their  “initials”,  “name  in  address  book”,  and  “username”.  For  
# example, if the user enters a first name of “John” and a last name of “Smith”, the program 
# should display “J.S.”, “John SMITH”, and “jsmith”.

def createNames(firstName, lastName):
    initials = firstName[0].upper() + "." + lastName[0].upper() + "."
    
    addressBook = firstName +" "+ lastName.upper()
    
    username = firstName[0].lower() + lastName.lower()

    return initials, addressBook, username 

def main():
    firstName = input("Enter your FIRST name: ")
    lastName = input("Enter your LAST name: ")
    initials, addressBook, username = createNames(firstName, lastName)
    print(f"Initials: {initials}")
    print(f"addressBook: {addressBook}")
    print(f"username: {username}")
main()

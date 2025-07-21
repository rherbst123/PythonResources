#Lets see how big the dict is...
phonebook = {'Jacob': '555-1111', 'john':'555-3333', 'carter': '666-3333'}



print(f"The phonebook has: {len(phonebook)} entries")


#To print all the names
for key in phonebook:
    print(key)


#To print all numbers without names
for key in phonebook:
    print(phonebook[key])


#To print all the information
for key in phonebook:
        #First, second parts
    print(key, phonebook[key])
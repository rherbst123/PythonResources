#Now we can apply if's and not's into the dictionaries

phonebook = {'Jacob': '555-1111', 'john':'555-3333', 'carter': '666-3333'}



if 'Jacob' in phonebook:
    
    print(phonebook['Jacob'])
    
# Same thing but NOT 
if 'Riley' not in phonebook:
    print("Riley is not found")
#Wow! Dictionaries, so usefull so nice!

phonebook = {'Jacob': '555-1111', 'john':'555-3333', 'carter': '666-3333'}

#The key values, "Names" are strings, values can be of any type though
print(phonebook['Jacob'])


#Since the key in this case was a string. 
#We can enter it as an input and get what we need
#Keys can also be, ints, floats or whatever you want
#Lists can NOT be a key in  a dictionary though
name = input("Enter the name to get the number: ")

print(phonebook[name])


#Adding and deleting elements in a dict.

#Creating our dict
phonebook = {'Jacob': '555-1111', 'john':'555-3333', 'carter': '666-3333', 'Mali': '812-3234'}

#Manually adding a name and number
phonebook['Bob'] = '654-8977'



#Wow bob is added
print(phonebook)


#Now lets add it by a user input
name = input("Enter a new name: ")
phone_num = input("Enter their phone number: ")

#Pretty Simple!!
phonebook[name] = phone_num

print(phonebook)

#We cannot add duplicate entries into the dictionary 
phonebook['Jacob'] = '555-1111'
#This will do nothing

#Deleting Jacob
del phonebook['Jacob']

#No jacob!
print("New",phonebook)


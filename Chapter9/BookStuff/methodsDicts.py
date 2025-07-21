# clear: Clears the contents of a dictionary.
# get: Gets the value associated with a specified key. If the key is not found, the method 
# does not raise an exception. Instead, it returns a default value.
# items: Returns all the keys in a dictionary and their associated values as a sequence of 
# tuples.
# keys: Returns all the keys in a dictionary as a sequence of tuples.
# pop: Returns the value associated with a specified key and removes that key-value 
# pair from the dictionary. If the key is not found, the method returns a default 
# value.
# popitem: Returns a randomly selected key-value pair as a tuple from the dictionary and 
# removes: that key-value pair from the dictionary.
# values: Returns all the values in the dictionary as a sequence of tuples

phonebook = {
    'Jacob': '555-1111',
    'john': '555-3333',
    'carter': '666-3333',
    'alice': '555-2222',
    'bob': '555-4444',
    'diana': '555-5555',
    'emily': '555-6666'
}
print(f"Full: {phonebook}")


"Clear the contents"

# phonebook.clear()
# print(f"Cleared: {phonebook}")

"Getting a specific number" 

# number = phonebook.get('john', 'Error!!!')
# print(number)

"Items method"

#Converted to a tuple!
# print(phonebook.items())

# for key, value in phonebook.items():
#     print(f"{key.upper()}: {value}")


"Keys"
#"Just prints the keys"
# for key in phonebook.keys():
#     print(key)

"Values"
"Just prints out the values"

# for value in phonebook.values():
#     print(value)

"Pop"


# phone_num = phonebook.pop('carter', 'Error')
# print(f"New: {phonebook}")

"Pop Item"

# "As we can see it removes emily from the list"
# key, value = phonebook.popitem()
# print(key, value)
# print(f"New: {phonebook}")




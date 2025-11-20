# 3.  Personal  Information Class
# Design a class that holds the following personal data: name, address, age, and phone num-
# ber. Write appropriate accessor and mutator methods. Also, write a program that creates 
# three instances of the class. One instance should hold your information, and the other two 
# should hold your friends’ or family members’ information


class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    
    # Accessor methods
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    # Mutator methods
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def __str__(self):
        return f"Name: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone: {self.__phone_number}"


# Create three instances
person1 = PersonalInformation("John Doe", "123 Main St", 25, "555-1234")
person2 = PersonalInformation("Jane Smith", "456 Oak Ave", 30, "555-5678")
person3 = PersonalInformation("Bob Johnson", "789 Pine Rd", 28, "555-9012")

# Display information
print("Person 1:")
print(person1)
print("\nPerson 2:")
print(person2)
print("\nPerson 3:")
print(person3)
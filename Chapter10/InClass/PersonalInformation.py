# 3.  Personal  Information Class
# Design a class that holds the following personal data: name, address, age, and phone num-
# ber. Write appropriate accessor and mutator methods. Also, write a program that creates 
# three instances of the class. One instance should hold your information, and the other two 
# should hold your friends’ or family members’ information

class PersonalInformation:
        def __init__(self, name, address, age, phoneNumber):
            self.__name = name
            self.__address = address
            self.__age = age
            self.__phoneNumber = phoneNumber

        #accessor Methods
        def get_name(self):
            return self.__name
        
        def get_address(self):
            return self.__address
        
        def get_age(self):
            return self.__age
        
        def get_phoneNumber(self):
            return self.__phoneNumber
        

        #Mutator Methods
        def set_name(self, name):
            self.__name = name

        def set_address(self, address):
            self.__address = address

        def set_age(self, age):
            self.__age = age
        
        def set_phoneNumber(self, phoneNumber):
            self.__phoneNumber = phoneNumber

        
        def __str__(self):
            return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, PhoneNumber: {self.__phoneNumber}"



person1 = PersonalInformation("Billy Bob", "123 Main Street", 21, "122-1234")
person2 = PersonalInformation("Some Guy", "5676 Oak Steet", 45, "545-3212")

print(person1)
print(person2)

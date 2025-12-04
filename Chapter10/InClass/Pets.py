# 1.  Pet Class
# Write a class named Pet, which should have the following data attributes:
# • _ _name (for the name of a pet)
# • _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, 
# and ‘Bird’)
# • _ _age (for the pet’s age)
# The Pet class should have an _ _init_ _ method that creates these attributes. It should also 
# have the following methods:
# • set_name
# This method assigns a value to the _ _name field.
# • set_animal_type
# This method assigns a value to the _ _animal_type field.
# • set_age
# This method assigns a value to the _ _age field.
# • get_name
# This method returns the value of the _ _ name field.
# • get_animal_type
# This method returns the value of the _ _animal_type field.
# • get_age
# This method returns the value of the _ _age field.
# The Pet class
# Once  you  have  written  the  class,  write  a  program  that  creates  an  object  of  the  class  and  
# prompts  the  user  to  enter  the  name,  type,  and  age  of  his  or  her  pet.  This  data  should  be  
# stored  as  the  object’s  attributes.  Use  the  object’s  accessor  methods  to  retrieve  the  pet’s  
# name, type, and age and display this data on the screen


class Pet:
    def __init__(self, name = '', animal_type = '', age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age
    

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    


def main():
    user_pet = Pet()


    name = input("What is your pets name?: ")
    animal_type = input("What kind of animal do you have?: ")
    age = int(input("How old is your pet?: "))

    #Store the user inputs
    user_pet.set_name(name)
    user_pet.set_animal_type(animal_type)
    user_pet.set_age(age)

    print("Your pets name is:")
    print(f"{user_pet.get_name()}")
    print("Your pets is a:")
    print(f"{user_pet.get_animal_type()}")
    print("Your pets age is:")
    print(f"{user_pet.get_age()}")

main()
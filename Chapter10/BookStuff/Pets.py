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
    def __init__(self, name='', animal_type='', age=0):
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
    # Create a Pet object
    my_pet = Pet()
    
    # Get pet information from user
    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter your pet's age: "))
    
    # Store data using setter methods
    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)
    
    # Display pet information using getter methods
    print("\nHere is the data you entered:")
    print(f"Pet name: {my_pet.get_name()}")
    print(f"Animal type: {my_pet.get_animal_type()}")
    print(f"Pet age: {my_pet.get_age()}")


if __name__ == '__main__':
    main()
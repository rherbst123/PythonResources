class person:
                #You always need the self
    def __init__(self, name, age):
        self.name = name
        self.age = age


personInfo1 = person("John",36)

name = input("Enter your name: ")
age = input("Enter your age: ")
personInfo2 = person(name, age)


print(personInfo1.name, personInfo1.age)
print(personInfo2.name, personInfo2.age)
#In Python, self is a conventional name for 
# the first parameter in instance methods within a class. 
# It is not a keyword, but a widely adopted naming convention.
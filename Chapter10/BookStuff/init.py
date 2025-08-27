class person:
                #You always need the self
    def __init__(self, name, age):
        self.name = name
        self.age = age


personInfo = person("John",36)

print(personInfo.name, personInfo)

#In Python, self is a conventional name for 
# the first parameter in instance methods within a class. 
# It is not a keyword, but a widely adopted naming convention.
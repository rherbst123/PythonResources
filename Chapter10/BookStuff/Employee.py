# 4.  Employee Class
# Write a class named Employee that holds the following data about an employee in attrib-
# utes: name, ID number, department, and job title.
# Once you have written the class, write a program that creates three Employee objects to 
# hold the following data:
# Name ID Number Department Job Title
# Susan Meyers 47899 Accounting Vice President
# Mark Jones 39119 IT Programmer
# Joy Rogers 81774 Manufacturing Engineer
# The  program  should  store  this  data  in  the  three  objects,  then  display  the  data  for  each  
# employee on the screen.


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print()

def main():
    # Create three Employee objects
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    
    # Display data for each employee
    emp1.display()
    emp2.display()
    emp3.display()

if __name__ == "__main__":
    main()
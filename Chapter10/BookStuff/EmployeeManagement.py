import pickle
import os

# 7.  Employee Management System
# This  exercise  assumes  you  have  created  the  Employee  class  for  Programming  Exercise  4.  
# Create a program that stores Employee objects in a dictionary. Use the  employee ID num-
# ber as the key. The program should present a menu that lets the user perform the following 
# actions:
# • Look up an employee in the dictionary
# • Add a new employee to the dictionary
# • Change an existing employee’s name, department, and job title in the dictionary
# • Delete an employee from the dictionary
# • Quit the program
# When the program ends, it should pickle the dictionary and save it to a file. Each time the 
# program starts, it should try to load the pickled dictionary from the file. If the file does not 
# exist, the program should start with an empty dictionary.



# Employee class definition
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    
    def set_name(self, name):
        self.__name = name
    
    def set_id_number(self, id_number):
        self.__id_number = id_number
    
    def set_department(self, department):
        self.__department = department
    
    def set_job_title(self, job_title):
        self.__job_title = job_title
    
    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id_number
    
    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__job_title

def display_menu():
    print('\n--- Employee Management System ---')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an employee\'s information')
    print('4. Delete an employee')
    print('5. Quit')

def lookup_employee(employees):
    id_number = input('Enter employee ID number: ')
    if id_number in employees:
        emp = employees[id_number]
        print(f'\nName: {emp.get_name()}')
        print(f'ID: {emp.get_id_number()}')
        print(f'Department: {emp.get_department()}')
        print(f'Job Title: {emp.get_job_title()}')
    else:
        print('Employee not found.')

def add_employee(employees):
    name = input('Enter name: ')
    id_number = input('Enter ID number: ')
    if id_number in employees:
        print('An employee with that ID already exists.')
        return
    department = input('Enter department: ')
    job_title = input('Enter job title: ')
    employees[id_number] = Employee(name, id_number, department, job_title)
    print('Employee added successfully.')

def change_employee(employees):
    id_number = input('Enter employee ID number: ')
    if id_number in employees:
        emp = employees[id_number]
        name = input('Enter new name: ')
        department = input('Enter new department: ')
        job_title = input('Enter new job title: ')
        emp.set_name(name)
        emp.set_department(department)
        emp.set_job_title(job_title)
        print('Employee information updated.')
    else:
        print('Employee not found.')

def delete_employee(employees):
    id_number = input('Enter employee ID number: ')
    if id_number in employees:
        del employees[id_number]
        print('Employee deleted.')
    else:
        print('Employee not found.')

def main():
    employees = {}
    
    while True:
        display_menu()
        choice = input('Enter your choice (1-5): ')
        
        if choice == '1':
            lookup_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            change_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

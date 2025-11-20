from datetime import date

# 6.  Patient Charges
# Write a class named Patient that has attributes for the following data:
# • First name, middle name, and last name
# • Address, city, state, and ZIP code
# • Phone number
# • Name and phone number of emergency contact
# The Patient class’s _ _init_ _ method should accept an argument for each attribute. The 
# Patient class should also have accessor and mutator methods for each attribute.
# Next,  write  a  class  named  Procedure  that  represents  a  medical  procedure  that  has  been  
# performed on a patient. The Procedure class should have attributes for the following data:
# • Name of the procedure
# • Date of the procedure
# • Name of the practitioner who performed the procedure
# • Charges for the procedure
# The  Procedure  class’s  _  _init_  _  method  should  accept  an  argument  for  each  attribute.  
# The Procedure class should also have accessor and mutator methods for each attribute.
# Next, write a program that creates an instance of the Patient class, initialized with sample 
# data. Then, create three instances of the Procedure class, initialized with the following data:
# Procedure #1: Procedure #2: Procedure #3:
# Procedure name: Physical Exam
# Date: Today’s date
# Practitioner: Dr. Irvine
# Charge: 250.00
# Procedure name: X-ray
# Date: Today’s date
# Practitioner: Dr. Jamison
# Charge: 500.00
# Procedure name: Blood test
# Date: Today’s date
# Practitioner: Dr. Smith
# Charge: 200.00
# The program should display the patient’s information, information about all three of the 
# procedures, and the total charges of the three procedures



class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, 
                 phone_number, emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone
    
    # Accessor methods
    def get_first_name(self):
        return self.__first_name
    
    def get_middle_name(self):
        return self.__middle_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_address(self):
        return self.__address
    
    def get_city(self):
        return self.__city
    
    def get_state(self):
        return self.__state
    
    def get_zip_code(self):
        return self.__zip_code
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_emergency_contact_name(self):
        return self.__emergency_contact_name
    
    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone
    
    # Mutator methods
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    def set_address(self, address):
        self.__address = address
    
    def set_city(self, city):
        self.__city = city
    
    def set_state(self, state):
        self.__state = state
    
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name
    
    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner, charges):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner = practitioner
        self.__charges = charges
    
    # Accessor methods
    def get_procedure_name(self):
        return self.__procedure_name
    
    def get_procedure_date(self):
        return self.__procedure_date
    
    def get_practitioner(self):
        return self.__practitioner
    
    def get_charges(self):
        return self.__charges
    
    # Mutator methods
    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name
    
    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date
    
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner
    
    def set_charges(self, charges):
        self.__charges = charges


def main():
    # Create a Patient instance
    patient = Patient("John", "Michael", "Smith", "123 Main St", "Springfield", 
                     "IL", "62701", "555-1234", "Jane Smith", "555-5678")
    
    # Create three Procedure instances
    today = date.today().strftime("%m/%d/%Y")
    
    procedure1 = Procedure("Physical Exam", today, "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", today, "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", today, "Dr. Smith", 200.00)
    
    # Display patient information
    print("Patient Information:")
    print(f"Name: {patient.get_first_name()} {patient.get_middle_name()} {patient.get_last_name()}")
    print(f"Address: {patient.get_address()}")
    print(f"City, State ZIP: {patient.get_city()}, {patient.get_state()} {patient.get_zip_code()}")
    print(f"Phone: {patient.get_phone_number()}")
    print(f"Emergency Contact: {patient.get_emergency_contact_name()} ({patient.get_emergency_contact_phone()})")
    print()
    
    # Display procedure information
    procedures = [procedure1, procedure2, procedure3]
    for i, proc in enumerate(procedures, 1):
        print(f"Procedure #{i}:")
        print(f"  Name: {proc.get_procedure_name()}")
        print(f"  Date: {proc.get_procedure_date()}")
        print(f"  Practitioner: {proc.get_practitioner()}")
        print(f"  Charge: ${proc.get_charges():.2f}")
        print()
    
    # Calculate and display total charges
    total_charges = sum(proc.get_charges() for proc in procedures)
    print(f"Total Charges: ${total_charges:.2f}")


if __name__ == "__main__":
    main()
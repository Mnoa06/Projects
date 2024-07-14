# Explanation of key concepts:

# List Comprehension: Used to create lists of patients and doctors.
# Searching Algorithm: A simple algorithm to find and assign a doctor to a patient.
# Unit Testing: Although not explicitly demonstrated here, unit tests can be written for the methods of each class.
# For Loops: For loops are used to iterate over patients and doctors.
# Inheritance: The Patient and Doctor classes inherit from the Person class.
# Polymorphism: The display_info method is overridden in both Patient and Doctor classes.
# Abstraction: The Person class is used for abstraction, as both Patient and Doctor share common attributes.
# Encapsulation: Attributes of Person, Patient, and Doctor classes are encapsulated.

#Step 1
# Create a new Python file (e.g., hospital_management.py).
# Define the Person class with attributes (name and age).

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Step 2
#Create the Patient class that inherits from Person.
# Add an attribute condition for the patient's health condition.
# Override the display_info method for polymorphism.

class Patient(Person):
    def __init__ (self, name, age, condition):
        super().__init__(name, age)
        self.condition = condition
        
    def display_info(self):
        print(f"Patient: {self.name}, Age: {self.age}, Condition: {self.condition}")
        
# Create the Doctor class that also inherits from Person.
# Add an attribute specialty for the doctor's specialty.
# Override the display_info method for polymorphism.

class Doctor(Person):
    def __init__(self, name, age, specialty):
        super(). __init__(name,age)
        self.specialty = specialty
    def display_info(self):
        print(f"Doctor: {self.name}, Age: {self.age}, Specialty: {self.specialty}")
        
        
# Create the Hospital class with attributes (name, patients, doctors, patient_queue, doctor_stack).
# Add methods to admit patients, assign doctors, and treat patients.
from queue import Queue
from collections import deque

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.patient_queue = Queue()
        self.doctor_stack = deque()
        
    def admit_patient(self, patient):
        self.patients.append(patient)
        self.patient_queue.put(patient)
        print(f"{patient.name} has been admitted to {self.name}")
        
    def assign_doctor(self, doctor):
        self.doctors.append(doctor)
        self.doctor_stack.append(doctor)
        print(f"{doctor.name} has been assigned to {self.name}")
        
    def treat_patients(self):
        while not self.patient_queue.empty() and self.doctor_stack:
            patient = self.patient_queue.get()
            doctor = self.doctor_stack.pop()
            print(f"{doctor.name} is treating {patient.name} for {patient.condition}")
            

# In the same file, create an instance of the Hospital class.
# Use list comprehension to create patients and doctors.
# Admit patients and assign doctors.
# Treat patients.
# Display patient and doctor information.

if __name__ == "__main__":
    #create a hospital
    general_hospital = Hospital("General Hospital")
    
    # Create patients and doctors using list comprehension
    patients = [Patient(f"Patient_{i}", 25 + i, f"Condition_{i}") for i in range (1,6)]
    doctors = [Doctor(f"Doctor_{i}", 30 + i, f"Specialty_{i}") for i in range(1, 4)]
    
    #admit patients and assign docotrs
    for patient in patients:
        general_hospital.admit_patient(patient)
        
    for doctor in doctors:
        general_hospital.assign_doctor(doctor)
        
    #treat patients
    general_hospital.treat_patients()
    
    #Display patient and doctor information
    
    for patient in general_hospital.patients:
        patient.display_info()
        
    for doctor in general_hospital.doctors:
        doctor.display_info()
        
          
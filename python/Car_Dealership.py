# Create a new Python file (e.g., car_dealership.py).
# Define the Vehicle class with attributes (make, model, year, and price) and a method display_info
# that prints information about the vehicle.

class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    
    def display_info(self):
        pass

# Create the Car class that inherits from the Vehicle class.
# Add a new attribute num_doors to the Car class.
# Override the display_info method to include information specific to cars.

class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors):
        super().__init__ (make, model, year, price)
        self.num_doors = num_doors
    
    def display_info(self):
        print(f"{self.year} {self.make}{self.model} - {self.num_doors} doors - ${self.price}")

# Create the Truck class that also inherits from the Vehicle class.
# Add a new attribute payload_capacity to the Truck class.
# Override the display_info method to include information specific to trucks.

class Truck (Vehicle):
    def __init__(self, make, model, year, price, payload_capacity):
        super(). __init__(make,model,year,price)
        self.payload_capacity = payload_capacity
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - Payload Capacity: {self.payload_capacity} - ${self.price}")
        
class Motorcycle(Vehicle):
    def __init__ (self, make, model, year, price, color):
        super(). __init__(make,model, year,price)
        self.color = color
        
    def display_info(self):
        print(f"{self.year} {self.make} {self.model} - Customerized Color {self.color}" )

# Create the Customer class with attributes (name, email) and an attribute owned_vehicle.
# Add a method purchase_vehicle that allows a customer to purchase a vehicle.        
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.owned_vehicle = None
    
    def purchase_vehicle(self, vehicle):
        self.owned_vehicle = vehicle
        print(f"{self.name} has purchased a {vehicle.year} {vehicle.make} {vehicle.model}")

# Create the Dealership class with attributes (name and inventory).
# Add methods add_vehicle to add a vehicle to the inventory and display_inventory to print the dealership's inventory.
class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        
    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)
        
    def display_inventory(self):
        print(f"Inventory at {self.name} Dealership: ")
        for vehicle in self.inventory:
            vehicle.display_info()

# Create instances of the classes and demonstrate how they interact
if __name__ == "__main__":
    # create vehicles
    car1 = Car("Toyota", "Camry", 2022, 25000, 4)
    truck1 = Truck ("Ford", "F-150", 2022,35000,2000)
    car2= Car("Mazda", "CX-9", 2023, 35000, 4)
    bike1 = Motorcycle("Kawaski", "Zx-10r Ninja", 2021, 8000, "red")
    # create customer
    customer1 = Customer("Marbin Noahh", "Marbin.noahh@gmail.com")
    customer2 = Customer("kristen Noahh", "kristen.Noahh@gmail.com")
    print()
    # create dealership
    dealership1 = Dealership("Best Cars")
    
    #add vehicles to the dealership inventory
    dealership1.add_vehicle(car1)
    dealership1.add_vehicle(truck1)
    dealership1.add_vehicle(car2)
    dealership1.add_vehicle(bike1)
    print()
    # display the dealersip's inventory
    dealership1.display_inventory()
    print()
    # Customer purchases a vehicle
    customer1.purchase_vehicle(car1)
    customer2.purchase_vehicle(car2)
    customer1.purchase_vehicle(bike1)
    print()
    # Display the updated dealership's inventory
    dealership1.display_inventory()
    
      

#Explanation of key concepts:

# Import: The os module is imported for working with file paths.
# Open File: The program uses the open function to read from and write to text files.
# While Loop: The program uses a while loop to read lines from a file until the end is reached.
# For Loop: For loops are used to iterate over the inventory and display or manipulate product information.
# Sorting Algorithms: The sort_inventory method uses the sort method with a custom 
# key function to sort the inventory based on the specified key.
# If-Else Statement: If-else statements are used to check conditions, 
# such as whether a product is found, if there is enough quantity to sell, etc.


#Create a new Python file (e.g., retail_business.py).
#Define the Product class with attributes (product_id, name, price, and quantity).
#Add a method display_info to print information about the product
#Define the Product class
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

#Create the RetailBusiness class with attributes (name and inventory).
# Add methods to load, save, display, add, and sell products
# Implement a method to sort the inventory based on a specified key.        
import os
 
class  RetailBusiness:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def load_inventory(self, file_path):
        #Use "With open" to safely open and close file
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                for line in file:
                    #Split the line and create a Product insance
                    product_id, name, price, quantity = line.strip().split(",")
                    product = Product(int(product_id), name, float(price), int(quantity))
                    self.inventory.append(product)
                    
    def save_inventory(self, file_path):
        with open(file_path, "w") as file:
            for product in self.inventory:
                file.write(f"{product.product_id},{product.name},{product.price},{product.quantity}\n")
                
    def display_inventory(self):
        print(f"Inventory at {self.name}:")
        for product in self.inventory:
            product.display_info()
            
    def add_product(self, product):
        self.inventory.append(product)
        
    def sell_product(self,product_id, quantity):
        for product in self.inventory:
            if product.product_id == product_id:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Sold {quantity} units of {product.name}")
                else:
                    print("Not enough quantity available")
                break
        else:
            print("Product not found")
    
    def sort_inventory(self, key = "name"):
        self.inventory.sort(key = lambda x: getattr(x,key))

# In the same file, create an instance of RetailBusiness.
# Load the initial inventory from a file.
# Display the initial inventory.
# Add a new product.
# Sell a product.
# Display the updated inventory.
# Sort the inventory.
# Display the sorted inventory.
# Save the updated inventory to a file.

      
if __name__ == "__main__":
    #Create a retail business/ create an instance of the retail business
    retail_store = RetailBusiness("Electronics World")
    
    #Load Inititial inventory from the file
    retail_store.load_inventory("inventory.text")
    
    #Display the inital inventory
    retail_store.display_inventory()
    
    #add new product
    new_product1 = Product(101, "Laptop", 1200.0, 20)
    new_product2 = Product(102, "Desktop", 1500.0, 15)
    retail_store.add_product(new_product1)
    retail_store.add_product(new_product2)
    
    ##display the updated inventory
    retail_store.display_inventory()
    #Sell a product
    retail_store.sell_product(101,5)
    
    #add another new product
    new_product3 = Product(105, "Keyboard", 200.0, 50)
    retail_store.add_product(new_product3)
    
    ##display the updated inventory
    retail_store.display_inventory()
    
    #Sort inventory by the product name
    retail_store.sort_inventory(key = "name")
    
    #Sell a product
    retail_store.sell_product(101,10)
    retail_store.sell_product(105, 25)
    #display the sorted inventory
    retail_store.display_inventory()
    
    #save the updated inventory to the file
    retail_store.save_inventory("updated_inventry.text")
    
        
    
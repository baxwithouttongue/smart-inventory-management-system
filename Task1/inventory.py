# This is the brain of this Smart Inventory Management System.
# This is the program to integrate all the other programs to make the system work.

class SmartInventorySystem:
    def __init__(self):         # Initaliza the system and prepare the data
        # Set up containers for product's lists, user's and supplier's dictionaries
        self.users = {}         # Prepare a dictionary to store the user data
        self.products = []      # Prepare a list to store the product data
        self.suppliers = {}     # Prepare a dictionary to store supplier data
        self.prepare_files ()   # Load data from employee, product and supplier files

    def prepare_files(self):
        # Load employee data from employee_role.csv
        
        # Load product data from product.csv

        # Load supplier data from supplier.csv

        pass
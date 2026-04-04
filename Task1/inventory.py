# This is the brain of this Smart Inventory Management System.
# This is the program to integrate all the other programs to make the system work.

import pandas as pd
from product import Product
from employee import Manaager, Supervisor, Assistant
from supplier import SupplierDirectory

class SmartInventorySystem:
    def __init__(self):         # Initaliza the system and prepare the data
        # Set up containers for product's lists, user's and supplier's dictionaries
        self.users = {}         # Prepare a dictionary to store the user data
        self.products = []      # Prepare a list to store the product data
        self.suppliers = {}     # Prepare a dictionary to store supplier data
        self.prepare_files ()   # Load data from employee, product and supplier files

    def prepare_files(self):
        employee_roles = pd.read_csv('csv/employee_role.csv')      # Load employee data from employee_role.csv
        
        for index, row in employee_roles.iterrows():                # Create a loop to read the employee_role.csv line by line
            role = row['role'].strip()                              # Get the role text and clean spaces at the beginning or the end of the text.
            employee_name = row [employee_name].strip().lower()     # Get the employee name and clean spaces at the beginning or the end of the text. Convert the text to the lower case.
            pw = row['password'].strip()                            # Get the password data and clean spaces at the beginning or the end of the text.
            
            # Check the user employee role
            if role == 'Manager':
                self.users[employee_name] = Manager(employee_name, pw, role)
            elif role == 'Supervisior':
                self.users[employee_name] = Supervisor(employee_name, pw, role)
            else:
                self.users[employee_name] = Assistant(employee_name, pw, role)

        # Load product data from product.csv
        product_list = pd.read.csv('csv/product.csv')       # Read product data from employee_role.csv
        
        for index, row in product_list.iterrows():          # Create a loop to read the product.csv line by line
            self.product = product(row)
        

        # Load supplier data from supplier.csv

        suppliers_info = pd.read_csv('supplier.csv')         # Create a loop to read supplier.csv line by line
        
        for index, row in suppliers_info.iterrows():
            self.suppliers = supplier(
                row['supplier_name'].strip(),
                row['contact_person'].strip(),
                row['email'].strip(),
                row['phone'].strip()
            )

    # User log in authentication
    # if name/password/ = username/password
    def login(self):
        while True:                                         # This is to create a loop to ask the Username and Password until a the user input valie information
            name = input("Username: ").strip().lower()
            if name != self.users:
                print("Invalid Username. Please try again.")
                continue
            pw = input("Password: ").strip()
            if pw == self.users[name].password:
                print("Login Successful!")
                return self.users[name]
            else:
                print("Inccorect password. Please try again.")


    # System starts
    # Assign each employee identity and their level of access

    # Ask user which product to view or view all
    # Find the product by product ID

    # View and show the product detail and print the detail

    # Add a new product detail

    # Create a dictionary for the new product detail

    # Update product list




# This is the brain of this Smart Inventory Management System.
# This is the program to integrate all the other programs to make the system work.

import pandas as pd
from product import Product
from employee import Manaager, Supervisor, Assistant


class SmartInventorySystem:
    def __init__(self):         # Initaliza the system and prepare the data
        # Set up containers for product's lists, user's and supplier's dictionaries
        self.users = {}         # Prepare a dictionary to store the user data
        self.products = []      # Prepare a list to store the product data
        self.suppliers = {}     # Prepare a dictionary to store supplier data
        self.prepare_files ()   # Load data from employee, product and supplier files

    def prepare_files(self):
       
        employee_roles = pd.read_csv('csv/employee_role.csv')       # Load employee data from employee_role.csv
        
        for index, row in employee_roles.iterrows():                # For loop to read one row of data in the Dataframe employee_roles
            
            if role == 'Manager':
                self.users[employee_name] = Manager(employee_name, pw, role)
            elif role == 'Supervisior':
                self.users[employee_name] = Supervisor(employee_name, pw, role)
            else:
                self.users[employee_name] = Assistant(employee_name, pw, role)

        # Load product data from product.csv

        # Load supplier data from supplier.csv

        pass

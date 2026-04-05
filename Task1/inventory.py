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
        while True:                                             # This is to create a loop to ask the Username and Password until a the user input valid information
            name = input('Username: ').strip().lower()          # Enter password with spaces removal and lower case text
            if name not in self.users:                          # Check if the username exists in the user dictionary
                print('Invalid Username. Please try again.')    # Print "Invalid Username and try again" if the user name is not found"
                continue                                        # Go back to ask again
            pw = input('Password: ').strip()                    # Ask the passowrd and clean spaces
            if pw == self.users[name].password:                 # Compare the password with the stored data
                print('Login Successful!')                      # Print "Login Successful" if it is right
                return self.users[name]                         # Return the user object
            else:
                print('Inccorect password. Please try again.')  # Print "Incorrect password and Please try again if it is wrong


    # System starts
    def start_system(self):                                     # This is where we start the Smart Inventory System
        print("****** This is the Smart Inventory Login *****") # Welcome message
        user = self.login()                                     # Call the login function to authenticate the user
        print(f"\n Welcome {user.get.name()}! [Role: {user.role}]")

        while True:                                             # To develop a loop to keep asking the user what action to do if the action is not "exit". 

            print('\nAvailable actions: ')                      # Available actions: View, Add, Update the product information
            actions = ['view']                                  # Every role is allowed to view the product information
            if user.permission('add'):                          # Permission level according to their roles: Manager(add, update, view), Supervisor(update and view), Assistant(view only)
                actions.append('add')                           # We need to create an empty list for the actions
            if user.permission('update'):
                actions.append('update')
            print(f"{', '.join(actions)}, 'or type 'exit'")     # Join three actions with 'comma' which is to separate actions, or tell the user to exit the action
            
            choice = input('Choose action: ')
            if choice == 'exit':                                # If a user chooses 'exit', the system will be ended
                break

            if choice not in actions:                           # If a user did not type the right word, it goes back to the loop and ask again.
                print('Invalid choice.')
                continue

            if choice == 'view':                                # If a user chooses 'view', call the function to show the product information
                self.show_products()
            
            if choice == 'add':                                 # If a user chooses 'add', call the function to add a new product information
                self.add_new_product()

            if choice == 'update':                              # If a user chooses 'update', call the function to update existing product information
                self.update_product()

    # Assign each employee identity and their level of access

    # Ask user which product to view or view all
    # Find the product by product ID

    # View and show the product detail and print the detail

    # Add a new product detail

    # Create a dictionary for the new product detail

    # Update product list




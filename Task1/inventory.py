# This is the brain of this Smart Inventory Management System.
# This is the program to integrate all the other programs to make the system work.

import pandas as pd
from product import Product
from employee import Manager, Supervisor, Assistant
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

    # Ask user which product to view or view all
    # Find the product by product ID

    def show_products(self):
        option = input("Enter Product ID to view or 'all' to view all: ")       #Ask for the usser to input 'view single product ID' or 'view all'
        if option == 'all':                                                     # If the user choose 'all', all product information are shown
            product_ids = [(prod.id) for prod in self.products]                 # Build a list of all product IDs.                 
            product_ids.sort()                                                  # Sort the list of product IDs alphabetically

            for pid in product_ids:                             # Create an outer loop to look at each sorted ID
                for prod in self.products:                      # Create an inner loop to find the product object to match the product ID
                    if prod.id == pid:                          # If found the matched product ID, then show the product information
                        self.show_product_details(prod)
                        break                                   # Once the matched product is found, then break to stop searching

        else:                                                   # Find a single product ID
            for pro in self.products:                           # Create a sinle loop to check each product ID
                if prod.id == option:                           # If the product ID is found, show the product detail
                    self.show_product_details(prod)
                    break                                       # Break the loop
            
            else:
                print('Product is not found.')                  # If there is no product ID matched after looping, print 'Product is not found'

    # View and show the product detail and print the detail
    def show_product_details(self, product):                    # Define show_product_details
        reorder_point = product.reorder_point()                 # Call the reorder_point method from the product object
        score = product.supplier_kpi_score()                    # Call the supplier_kpi_score from the product objct
        supplier_info = self.suppliers.get_supplier(product.supplier_name)      # Fetch full supplier detals from supplier database
        if product.stock <= reorder_point:                      # Check if the stock is less than or equal to the reorder point
            alert = '[!] RE-ORDER'                              # If the stock is less than or equal to the reorder point, it shows alert to the user
        else:                                                   # If the stock level is still above teh reorder point, then the program runs the else block
            alert = ''                                          # It prints nothing
        
        print(f"\nID: {product.id}, Name: {product.product_name}, Price: {product.price} HKD")          # Print the product's ID, name, price in Hong Kong Dollars
        print(f"Supplier: {product.supplier_name}, Contact: {supplier_info.get('contact_person','N/A')}, Email: {supplier_info.get('email','N/A')}")        # Print supplier details: name, contact person, and email
        print(f"Stock: {product.stock}, Safety Stock: {product.safety_stock}, Lead Time: {product.lead_time} days")    # Print inventory details: current stock, safety stock (buffer stock to avoid shortage) and lead time (days taken for restocking)
        print(f"Delivered: {product.delivered}, Returned: {product.returned}, KPI Score: {score:.2f}%{alert}")      # Print delivery and return product quantity information

    # Add a new product detail
    def add_new_product():                                      # Define a method called add_new_product inside class
        print("\n***** Add New Product *****")                  # Print 'Add New Product' to tell the user for entering new product detail
        pid = input('Product ID: ')                             # Enter Product ID
        product_name = input('Product Name: ')                  # Enter Product Name
        price = input('Price: ')                                # Enter Price
        supplier_name = input('Supplier: ')                     # Enter Supplier
        stock = input('Stock level: ')                          # Enter Stock Level
        safety = input('Safety Stock level: ')                  # Enter Safety Stock Level
        lead = input('Lead Time: ')                             # Enter Lead Time
        order_cost = input('Ordering Cost: ')                   # Enter Ordering Cost
        hold_cost = input('Holding Cost: ')                     # Enter Holding Cost
        delivered = input('Quantity delivered: ')               # Enter Quantity delivered
        returned = input('Quantity returned: ')                 # Enter Quantity returned

        # Create a dictionary for the new product called new_row
        new_row = {                                             # Create a container to prepare the data to be stored
            'product_id': pid,                                  # 'product_id' points to pid
            'product_name': product_name,                       # 'product_name' points to product_name
            'price (hkd)': price,                               # 'price (hkd)'points to price
            'supplier_name': supplier_name,                     # 'supplier_name'points to supplier_name, 
            'stock_level': stock,                               # 'stock_level' points to stock
            'safety_stock': safety,                             # 'safety_stock' points to safety
            'lead_time (days)': lead,                           # 'lead_time (days)' points to lead
            'ordering_cost': order_cost,                        # 'ordering_cost' points to order_cost
            'holding_cost': hold_cost,                          # 'holding_cost' points to hold_cost
            'quantity_delivered': delivered,                    # 'quantity_delivered' points to delivered
            'quantity_returned': returned                       # 'quantity_returned' points to returned
        }

    # Update product list
    def update_product(self):                                   # Define the function and prints 'Update Product' message
        print('\n***** Update Product *****')
        pid = input('Enter Product ID to update: ')             # Ask the user for the product ID

        # Find the product in the list
        product = None                                          # Product sets none at the beginning because no product has been found by default
        for prod in self.products:                              # Create a loop to go through the product detail
            if prod.id == pid:                                  # If the product ID is matched
                product = prod                                  # Then assign it to the product
                break                                           # Stop searching

        if not product:                                         # If the product ID is not matched
            print('Product is not found.')                      # Then print the product is not found
            return                                              # Return to stop the function right here

        # Show the chosen field
        print('Editable fields: product_name, price, supplier_name, stock_level, safety_stock, lead_time (days), ordering_cost, holding_cost, quantity_delivered, quantity_returned')
        field = input('Which field do you want to change? ')    # Show which field can be edited / update
        new_value = input('Enter new value: ')                  # Ask which field the user what to change

        # Update the chosen fields
        if field == 'product_name':                             # If the user choose product_name
            product.product_name = new_value                    # Then update the product_name with the new value
        elif field == 'price':                                  # If the user choose price
            product.price = float(new_value)                    # Then update the price with the new value
        elif field == 'supplier_name':                          # If the user supplier_name
            product.supplier_name = new_value                   # Then update the supplier_name with the new value
        elif field == 'stock_level':                            # If the user choose price
            product.stock = int(new_value)                      # Then update the price with the new value
        elif field == 'safety_stock':                           # If the user choose safety_stock
            product.safety_stock = int(new_value)               # Then update the safety_stock with the new value
        elif field == 'lead_time (days)':                       # If the user choose lead_time (days)
            product.lead_time = int(new_value)                  # Then update the lead_time (days) with the new value
        elif field == 'ordering_cost':                          # If the user choose ordering_cost
            product.ordering_cost = int(new_value)              # Then update the ordering_cost with the new value
        elif field == 'holding_cost':                           # If the user choose holding_cost
            product.holding_cost = int(new_value)               # Then update the holding_cost with the new value
        elif field == 'quantity_delivered':                     # If the user choose quantity_delivered
            product.delivered = int(new_value)                  # Then update the quantity_delivered with the new value
        elif field == 'quantity_returned':                      # If the user choose quantity_returned
            product.returned = int(new_value)                   # Then update the quantity_returned with the new value
        else:                                                   # If the user types the invalid field
            print('Invalid field.')                             # Then print 'Invalid Field'
            return                                              # Exit this function immediately
  

        



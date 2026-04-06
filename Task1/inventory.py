# This is the brain of this Smart Inventory Management System.
# This is the program to integrate all the other programs to make the system work.

import pandas as pd
from product import Product
from employee import Manager, Supervisor, Assistant
from supplier import Supplier, SupplierDirectory

# *****************************************************************************
# **    Main inventory system which manages users, products and suppliers    ** 
# *****************************************************************************

class SmartInventorySystem:                                         # Defines the main system class. This is the brain of the inventory management system
    def __init__(self):                                             # Creates a constructor to initaliza the new inventory system instance
       
        # Sets up containers for product's lists, user's and supplier's dictionaries
        self.users = {}                                             # Creates an empty user dictionary that will store User's identity for later authentication and permission checking
        self.products = []                                          # Creates an empty product list to store the product data
        self.suppliers = SupplierDirectory()                        # Creates supplier directory to manage supplier data
        self.prepare_files ()                                       # Load all ata from employee, product and supplier files

    def prepare_files(self):                                        # Defines data loading method

        # *************************
        # **    Load Employees   **
        # *************************
        
        employee_roles = pd.read.csv('csv/employee_role.csv')       # Uses Pandas library to open employee_role.csv and converts the entire spreadsheet into DataFrame stored in the variable employee_role
        employee_roles.columns = employee_roles.columns.str.lower().str.strip()     # Cleans spaces and converts all column headers to lowercase
        
        for index, row in employee_roles.iterrows():                # Creates a loop to read the employee_role.csv line by line
            role = row['role'].strip()                              # Gets user role (Manager, Supervisor, Assistant) and clean spaces
            employee_name = row['employee_name'].strip().lower()    # Gets the employee name, clean spaces and converts to lowercase
            pw = row['password'].strip()                            # Gets the password data and clean spaces
            
            # Check the user employee role to determine the user type
            if role == 'Manager':                                                   # Checks for Manager role
                self.users[employee_name] = Manager(employee_name, pw, role)        # Creates Manager object and stores in users dictionary
            elif role == 'Supervisor':                                              # Checks for Supervisor role
                self.users[employee_name] = Supervisor(employee_name, pw, role)     # Creates Supervisor object and stores in users dictionary
            else:                                                                   # By default, if user is not Manager or Supervisor, he must ba an Assistant
                self.users[employee_name] = Assistant(employee_name, pw, role)      # Creates Assistant object and stores in a uswers dictionary

        # *************************
        # **    Load Products    **
        # *************************

        product_list = pd.read.csv('csv/product.csv')               # Uses Pandas library to open product.csv and converts the entire spreadsheet into DataFrame stored in the variable product_list
        product_list.columns = product_list.columns.str.lower().str.strip()         # Cleans spaces and converts all column headers to lowercase

        for index, row in product_list.iterrows():                  # Create a loop to read the product.csv line by line
            self.products.append(Product(row))                      # Creates Product object to convert every row inside csv to a Product and adds it to the product list
        
        # *************************
        # **    Load Suppliers   **
        # *************************

        suppliers_info = pd.read_csv('supplier.csv')                # Uses Pandas library to open supplier.csv and converts the entire spreadsheet into DataFrame stored in the variable suppliers_info
        suppliers_info.columns = suppliers_info.columns.str.lower().str.strip()     # Cleans spaces and converts all column headers to lowercase

        for index, row in suppliers_info.iterrows():                # Creates a loop to read supplier.csv line by line
            self.suppliers.add_supplier(                            # Stores and saves every supplier's contact into the SupplierDirectory
                str(row['supplier_name']).strip(),                  # Ensures the data is treated as text and clean spaces
                str(row['contact_person']).strip(),                 
                str(row['email'].strip()).strip(),  
                str(row['phone']).strip()
            )

    # *******************************
    # **    Login Authentication   **
    # *******************************
    
    def login(self):                                            # Defines login method to manage user authentication
        
        while True:                                             # This is to create a loop to ask the Username and Password until a the user input valid information
            
            name = input('Username: ').strip().lower()          # Enters username with spaces removal and converts to lower case
            if name not in self.users:                          # Checks if the username exists in the user dictionary
                print('Invalid Username. Please try again.')    # Prints "Invalid Username and try again" if the user name is not found"
                continue                                        # Restarts the loop. Goes back to ask again
            
            pw = input('Password: ').strip()                    # Ask the passowrd and clean spaces
            if pw == self.users[name].password:                 # Compare the entered password with the stored data
                print('Login Successful!')                      # Print "Login Successful" if it is matched
                return self.users[name]                         # Return the user object and exits
            
            else:                                               # If password is incorrect
                print('Inccorect password. Please try again.')  # Then prints 'Incorrect password and Please try again' and the loop continues

    # *************************
    # **    System Starts    **
    # *************************

    def start_system(self):                                     # Defines main system loop
        print('****** This is the Smart Inventory Login *****') # Welcome message
        user = self.login()                                     # Calls the login function to authenticate the user
        print(f'\nWelcome {user.get.name()}! [Role: {user.role}]')      # Displays welcome message, user's name and role

        while True:                                             # To develop a loop to keep asking the user what action to do if the action is not "exit". 

            print('\nAvailable actions: ')                      # Available actions: View, Add, Update the product information
            actions = ['view']                                  # Every role is allowed to view the product information
                                                                # Permission level according to their roles: Manager(add, update, view), Supervisor(update and view), Assistant(view only)
            if user.permission('add'):                          # Checks 'add' permission. If user has 'add' permission
                actions.append('add')                           # Adds 'add' to the action list
            
            if user.permission('update'):                       # Checks 'update' permission. If user has 'update' permission
                actions.append('update')                        # Adds 'update' to the action list
            
            print(f"{', '.join(actions)}, 'or type 'exit'")     # Displays available actions and join three actions with 'comma' to separate them, or tell the user to 'exit' the action
            
            choice = input('Choose action: ').strip().lower()   # Gets user choice and clean spaces and converts to lower case
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
    
    
    # *************************
    # **    Search Engine   **
    # *************************

    def show_products(self):                                                            # Defines display method to show product information
        option = input("Enter Product ID to view or 'all' to view all: ").strip()       # Gets user option. Ask for the user to input 'view single product ID' or 'view all'
        if option.lower() == 'all':                                                     # Converts the option to lower case. If the user option is 'all' 
            product_ids = [prod.id.lower() for prod in self.products]                   # Creates lowercase product ID list and extracts all product IDs                
            product_ids.sort()                                                          # Sorts the list of product IDs alphabetically

            for pid in product_ids:                             # Create an outer loop to look at each sorted ID
                for prod in self.products:                      # Create an inner loop to find the product object to match the product ID
                    if prod.id.lower() == pid:                  # If the matched product ID is found
                        self.show_product_details(prod)         # Then shows the product information
                        break                                   # Once the matched product is found, then stop the inner loop and moves to the next product ID

        else:                                                   # Finds a single product ID
            for prod in self.products:                          # Create sa sinle loop to check each product ID
                if prod.id.lower() == option.lower():           # If the product ID (case insensitive) is found
                    self.show_product_details(prod)             # Shows the product detail
                    break                                       # Exits the loop
            
            else:                                               # If there is no product ID matched after looping
                print('Product is not found.')                  # Prints 'Product is not found'

    # *******************************
    # **    Show Product Details   **
    # *******************************

    def show_product_details(self, product):                                    # Defines show_product_details
        reorder_point = product.reorder_point()                                 # Calls the reorder_point method from the product object
        score = product.supplier_kpi_score()                                    # Calls the supplier_kpi_score from the product objct
        supplier_info = self.suppliers.get_supplier(product.supplier_name)      # Fetches full supplier detals from supplier database
        if product.stock <= reorder_point:                                      # Checks if the stock is less than or equal to the reorder point
            alert = '[!] RE-ORDER'                                              # If the stock is less than or equal to the reorder point, it shows alert to the user
        else:                                                                   # If the stock level is still above the reorder point, then the program runs the else block
            alert = ''                                                          # It prints nothing
        
        print(f'\nID: {product.id}, Name: {product.product_name}, Price: {product.price} HKD')                                                              # Displays the product's ID, name, price in Hong Kong Dollars
        print(f'Supplier: {product.supplier_name}, Contact: {supplier_info.get('contact_person','N/A')}, Email: {supplier_info.get('email','N/A')}')        # Uses .get and displays supplier details: name, contact person, and email
        print(f'Stock: {product.stock}, Safety Stock: {product.safety_stock}, Lead Time: {product.lead_time} days')                                         # Displays inventory details: current stock, safety stock (buffer stock to avoid shortage) and lead time (days taken for restocking)
        print(f'Delivered: {product.delivered}, Returned: {product.returned}, KPI Score: {score:.2f}%{alert}')                                              # Displays delivery and return product quantity information


    # **********************************
    # **    Add New Product Details   **
    # **********************************
    
    def add_new_product(self):                                      # Defines a method called add_new_product inside class
        print("\n***** Add New Product *****")                  # Displays 'Add New Product' to tell the user for entering new product detail
        pid = input('Product ID: ').strip()                     # Gets Product ID and cleans spaces
        product_name = input('Product Name: ').strip()          # Gets Product Name and cleans spaces
        price = float(input('Price (HKD): ').strip())           # Gets Price and cleans spaces
        supplier_name = input('Supplier: ').strip()             # Gets Supplier and cleans spaces
        stock = int(input('Stock level: ').strip())             # Gets Stock Level and cleans spaces
        safety = int(input('Safety Stock level: ').strip())     # Gets Safety Stock Level and cleans spaces
        lead = int(input('Lead Time: ').strip())                # Gets Lead Time and cleans spaces
        order_cost = int(input('Ordering Cost: ').strip())      # Gets Ordering Cost and cleans spaces
        hold_cost = int(input('Holding Cost: ').strip())        # Gets Holding Cost and cleans spaces
        delivered = int(input('Quantity delivered: ').strip())  # Gets Quantity delivered and cleans spaces
        returned = int(input('Quantity returned: ').strip())    # Gets Quantity returned and cleans spaces

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

        self.products.append(Product(new_row))                  # Adds new product to sel.product list

        # Creates a dictionary and save all products back to product.csv file
        
        product_data_list = [{                                  # Creates a new list and converts all products to the dictionaries
            'product_id': prod.id,                              # This part defines each product data should be match the detail in product.csv file
            'product_name': prod.product_name,
            'price (hkd)': prod.price,
            'supplier_name': prod.supplier_name,
            'stock_level': prod.stock,
            'safety_stock': prod.safety_stock,
            'lead_time (days)': prod.lead_time,
            'ordering_cost': prod.ordering_cost,
            'holding_cost': prod.holding_cost,
            'quantity_delivered': prod.delivered,
            'quantity_returned': prod.returned
            } 
            for prod in self.products
            ]
        
        pd.DataFrame(product_data_list).to_csv('product.csv', index = False)        # Saves the product_data_list to product.csv
        print('Product is added successfully!')                                     # Displays confirmation message

    # ******************************
    # **    Update Product List   **
    # ******************************

    def update_product(self):                                        # Defines update method to modify the existing product detail
        print('\n***** Update Product *****')                        # Displays 'Update Product' to tell the user to update the product detail
        pid = input('Enter Product ID to update: ').strip().lower()  # Gets the product ID, clean spaces and converts to lower case

        # Find the product in the list
        product = None                                          # Product sets none at the beginning because no product has been found by default
        for prod in self.products:                              # Create a loop to go through the product detail
            if prod.id.lower() == pid:                          # If the product ID is matched with cleaned spaces
                product = prod                                  # Then assign it to the product
                break                                           # Stop searching

        if not product:                                         # If the product ID is not matched
            print('Product is not found.')                      # Then displays the 'Product is not found'
            return                                              # Exits the method

        # Displays the editable field
        print('Editable fields: product_name, price, supplier_name, stock_level, safety_stock, lead_time (days), ordering_cost, holding_cost, quantity_delivered, quantity_returned')
        field = input('Which field do you want to change? ').strip().lower()    # Gets field name, cleans spaces and converts to lower case
        new_value = input('Enter new value: ').strip()                            # Gets new value and cleans spaces

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
            return                                              # Exits this function immediately
  
        # Creates a dictionary and save all products back to product.csv file

        product_data_list = [{                                  # Creates a new list and converts all products to the dictionaries
            'product_id': prod.id,                              # This part defines each product data should be match the detail in product.csv file
            'product_name': prod.product_name,
            'price (hkd)': prod.price,
            'supplier_name': prod.supplier_name,
            'stock_level': prod.stock,
            'safety_stock': prod.safety_stock,
            'lead_time (days)': prod.lead_time,
            'ordering_cost': prod.ordering_cost,
            'holding_cost': prod.holding_cost,
            'quantity_delivered': prod.delivered,
            'quantity_returned': prod.returned
            }
            for prod in self.products
            ]
        pd.DataFrame(product_data_list).to_csv('product.csv', index = False)     # Saves the product_data_list to product.csv
        print("Product updated successfully!")                                   # Displays confirmation message
        



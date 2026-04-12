# This is the blueprint for the Supplier and SupplierDirectory class
# It provides the objects and methods used by the inventory system

class Supplier:                                                         # Defines a class called Supplier and creates the blueprint for managing supplier objects
    def __init__(self, data):                                           # Creates a constructor method and create supplier object
        self.id = str(data['supplier_id']).strip()                      # Stores supplier ID and cleans spaces
        self.name = data['supplier_name'].strip()                       # Stores supplier name and cleans spaces
        self.contact = data['contact_person'].strip()                   # Stores contact person and cleans spaces
        self.email = data['email'].strip()                              # Stores email address and cleans spaces
        self.phone = data['phone'].strip()                              # Stores phone number and cleans spaces

class SupplierDirectory:                                                # Define a class called SupplierDirectory and creates a blueprint for managing multiple suppliers
    def __init__(self):                                                 # Creates a constructor methnod to initialize SupplierDirectory object
        self.suppliers = {}                                             # Creates an empty dictionary to store information about the supplier objects
    
    def add_supplier(self, supplier_name, contact, email, phone):       # Defines a method called add_supplier to add new supplier details to self.supplier dictionary
        self.suppliers[supplier_name] = {                               # Creates a dictionary called supplier_name to store contact, email and phone details
            "contact_person": contact.strip(),                          # Stores a contact person and cleans spaces
            "email": email.strip(),                                     # Stores an email and cleans spaces
            "phone": phone.strip()                                      # Stores a phone number and cleans spaces
        }                                                               # Closes the dictinary
        
    def get_supplier(self, supplier_name):                              # Defines a method called get_supplier to retrieve the supplier's name.
        return self.suppliers.get(supplier_name, {})                    # If the supplier exists, return the details of the supplier. If it cannot be found, return the empty dictionary





    

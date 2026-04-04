# This is the blueprint for the SupplierDirectory class.
# It provides the objects and methods used by the inventory system.

class SupplierDirectory:                # Define a class called SupplierDirectory

    def __init__(self):                 # Create a new SupplierDirectory object
        self.suppliers = {}             # Create an empty container to store information about the suppliers
    
    def add_supplier(self, supplier_name, contact, email, phone):
        self.suppliers[supplier_name] = supplier_name
        self.contact = contact
        self.email = email
        self.phone = phone
    
    def get_supplier(self, supplier_name):
        return





    
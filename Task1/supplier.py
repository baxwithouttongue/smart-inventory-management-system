# This is the blueprint for the SupplierDirectory class.
# It provides the objects and methods used by the inventory system.

class SupplierDirectory:                # Define a class called SupplierDirectory

    def __init__(self):                 # Create a new SupplierDirectory object
        self.suppliers = {}             # Create an empty container to store information about the suppliers
    
    def add_supplier(self, supplier_name, contact, email, phone):       # Define a method called add_supplier that stores supplier details to self.supplier dictionary.
        self.suppliers[supplier_name] = {
            "contact": contact,
            "email": email,
            "phone": phone
        }
        
    def get_supplier(self, supplier_name):  # Define a method called get_supplier to check the supplier's name.
        return self.suppliers.get(supplier_name, {})        # if the supplier exists, return the details of the supplier. If it cannot be found, return the empty dictionary for later use.





    
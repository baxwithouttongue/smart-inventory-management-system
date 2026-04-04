# This is the blueprint for the Supplier and SupplierDirectory class.
# It provides the objects and methods used by the inventory system.

class Supplier:                                                         # Define a class called Supplier
    def __init__(self, data):                                           # Create a constructor method and create supplier object
        self.id = str(data['supplier_id']).strip()                      # To clean spaces in Supplier ID
        self.name = data['supplier_name'].strip()                       # To clean spaces in Supplier name
        self.contact = data['contact_person'].strip()                   # To clean spaces in contact person
        self.email = data['email'].strip()                              # To clean spaces in email address
        self.phone = data['phone'].strip()                              # To clean spaces in phone number

class SupplierDirectory:                                                # Define a class called SupplierDirectory to manage multiple suppliers
    def __init__(self):                                                 # Create a constructor methnod and create SupplierDirectory object
        self.suppliers = {}                                             # Create an empty container to store information about the supplier objects
    
    def add_supplier(self, supplier_name, contact, email, phone):       # Define a method called add_supplier that stores new supplier details to self.supplier dictionary.
        self.suppliers[supplier_name] = {                               # Use supplier_name as a dictionary key an store contact, email and phone details in the same dictonary
            "contact_person": contact.strip(),                          # Save the contact 
            "email": email.strip(),
            "phone": phone.strip()
        }
        
    def get_supplier(self, supplier_name):                              # Define a method called get_supplier to check the supplier's name.
        return self.suppliers.get(supplier_name, {})                    # if the supplier exists, return the details of the supplier. If it cannot be found, return the empty dictionary for later use.





    
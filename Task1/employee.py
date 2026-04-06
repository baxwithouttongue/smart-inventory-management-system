# This is the class for defining all users who will use this system
# Different roles have different levels of permission to access and control the data

class User:                                                     # Defines the parent class and creates a blueprint for all user types
    def __init__(self, employee_name, password, role):          # Creates a constructor method to initialize a new user object with name, password and rold
        self.employee_name = employee_name                      # Stores and saves the user's name
        self.password = password                                # Stores and saves the user's password
        self.role = role                                        # Stores and saves the user's role

    def authenticate(self, password):                           # Checks if the entered password matches the stored password
        return self.password == password                        # Returns True if the password matches but False otherwise
    
    def get_name(self):                                         # Returns the user's name            
        return self.employee_name                               # Allows other parts of the program to retrieve the username   

    def permission(self, action):                               # No permission is allowed to access or control any data by default
        return False                                            # No access of any data for base user

class Manager(User):                                            # Defines Manager subclass which inherits all methods and attributes from User
    def permission(self, action):                               # Defines Manager's access level
        return action in ['add', 'update', 'view']              # Manager posseses a full permission to add, update and view products

class Supervisor(User):                                         # Defines Supervisor subclass which inherits from User
    def permission(self, action):                               # Defines Supervisor's access level
        return action in ['add', 'view']                        # Supervisor posseses a right to add and view the products but cannot update

class Assistant(User):                                          # Defines Assistant subclass which inhertits from User
    def permission(self, action):                               # Defines Assistant's access level
        return action == 'view'                                 # Assistant can only view products and cannot either add or update the product details
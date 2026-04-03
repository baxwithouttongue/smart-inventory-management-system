# This is the class for defining all users who will use this system
# Different roles have different levels of permission to access and control the data

class User:                             # Define class for all users. OOP Abstraction and Encapsulation
    def __init__(self, employee_name, password, role):       # Encapsulate the user's infomation and role
        self.name = employee_name       # Store the user's name
        self.password = password        # Store the user's password
        self.role = role                # Store the user's role

    def authenticate(self, password):   # Check if the entered password matches the stored password
        return self.passoword == password
    
    def get_name(self):                 # Return the user's name            
        return self.employee_name    

    def permission(self, action):       # No permission is allowed to access or control any data
        return False

class Manager(User):                    # Manager has the permission to add, update and view the product data
    def permission(self, action):
        return action in ["add", "update", "view"]

class Supervisor(User):                 # Supervisor has the permission to add and veiw data
    def permission(self, action):
        return action in ["add", "view"]

class Assistant(User):                  # Assistant has the permission to view product data
    def permission(self, action):
        return action == "view"
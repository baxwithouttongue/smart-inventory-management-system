#This is the class for defining all users who will use this system
#Different roles have different levels of permission to access and control the data

class User:         
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def authenticate(self, password):
        return self.password == password

    def get_name(self):
        return self.name

    def permission(self, action):
        return False

class Manager(User):
    def permission(self, action):
        return action in ["add", "update", "view"]

class Supervisor(User):
    def permission(self, action):
        return action in ["add", "view"]

class Assistant(User):
    def permission(self, action):
        return action == "view"
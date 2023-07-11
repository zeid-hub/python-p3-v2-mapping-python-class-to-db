from __init__ import CURSOR, CONN

class Department:

    # Define a dictionary to store class instances for subsequent lookup when mapping a table row to a class instance.
    all = {}
    
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

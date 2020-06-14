# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
    
    # Define attributes
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = []
        

    # object.__str__ method to allow for direct printing of object contents
    def __str__(self):
        return f'Name: {self.name} -> Desc: {self.description} -> Items: {self.items}'

    # Gets Description
    def get_description(self):
        return self.description

    #Sets Items
    def set_items(self, items):
        self.items.extend(items)

 
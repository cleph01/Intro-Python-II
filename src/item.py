class Item:
    def __init__(self, name, description):
    
    # Define Attributes
        self.name = name
        self.description = description

    # object.__str__ method to allow for direct printing of object contents
    def __str__(self):
        return f'Item Name: {self.name} - Item Description: {self.description}'

    # Prints the Item Name on_take
    def on_take(self):
        print(f'\n You have picked up a {self.name}')

    # Prints the Item Name on_drop
    def on_drop(self):
        print(f'\n You have dropped the {self.name}')
    
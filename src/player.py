# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
    
    # Define Attributes
        self._name = name
        self._current_room = current_room

    # object.__str__ method to allow for direct printing of object contents
    def __str__(self):
        return f'Current Room: {self._current_room}'

    # Define Methods
    
    # Set Current Room
    def _set_current_room(self, new_room):
        if not new_room:
            raise Exception("Invalid Room")
        self._current_room = new_room
    def _get_current_room(self):
        return self._current_room

    # Set Name
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    def _get_name(self):
        return self._name

    # property keyword wires up the getter and setter    
    room = property(_get_name, _set_name)
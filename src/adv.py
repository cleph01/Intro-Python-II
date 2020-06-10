from room import Room
from player import Player

import textwrap


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# for k,v in room.items():
#     print("Key: ",k, " - Value: ", v.w_to)
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player("player_1", room["outside"])

# print("Print Player: ", player)

# Write a loop that:
#
quit = False


while quit == False:

    current_room = player._get_current_room()

    # * Prints the current room name

    print("Current Room Name: ", current_room.name)
   
    # * Prints the current description (the textwrap module might be useful here).

    print("Current Room Description: ", textwrap.fill(current_room.description, width=50))


    # * Waits for user input and decides what to do.

    x = input("\n Enter the next direction (i.e. n, s, e, w): ")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    if (x.lower() == 'n'):
        
        try:
            
            player._set_current_room(current_room.n_to)

        except:

            print("Invalid Room, Try Again")
            x = input("\n Enter the next direction (i.e. n, s, e, w): ")

    elif (x.lower() == 's'):
        
        try:

            player._set_current_room(current_room.s_to)

        except:

            print("Invalid Room, Try Again")
            x = input("\n Enter the next direction (i.e. n, s, e, w): ")

    elif (x.lower() == 'e'):
        
        try:
        
            player._set_current_room(current_room.e_to)

        except:

            print("Invalid Room, Try Again")
            x = input("\n Enter the next direction (i.e. n, s, e, w): ")

    elif (x.lower() == 'w'):

        try:

            player._set_current_room(current_room.w_to)

        except:

            print("Invalid Room, Try Again")
            x = input("\n Enter the next direction (i.e. n, s, e, w): ")

    elif (x.lower() == 'q'):
        quit = True
        print("Game Has Been Quit")
    else:
        print("Error: That Move Is Not Allowed")





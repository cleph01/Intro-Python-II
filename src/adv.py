from room import Room
from player import Player
from item import Item

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


# START Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# END Link rooms together

# START Define Items
items = {
"map" : Item("map","So you can find your way around"),
"sword" : Item("sword","A Warrior's Tool"),

"coins" : Item("coins", "Money to Buy Things"),
"food" : Item("food", "In case you get hungry"),

"rope" : Item("rope", "To Climb"),
"telescope" : Item("telecope", "So you can see far"),

"torch" : Item("torch", "To see in the dark"),
"potion" : Item("potion", "Gives you a boost of energy"),

"treasure" : Item("treasure", "You found it")
}
# END Define Items

# START Set Items in Rooms
room['outside'].set_items([items["sword"], items["map"]])
room['foyer'].set_items([items["coins"], items["food"]])
room['overlook'].set_items([items["rope"], items["telescope"]])
room['narrow'].set_items([items["torch"], items["potion"]])
room['treasure'].set_items([items["treasure"]])
# END Set Items in Rooms

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player("player_1", room["outside"])


# Write a loop that:
#
quit = False


while quit == False:

    current_room = player._get_current_room()

    # * Prints the current room name

    current_room_items = ''

    if (len(current_room.items) == 0):
        
        current_room_items = "Room is Empty"

    else:

        for item in current_room.items:

            current_room_items = current_room_items + item.name + ", "


    print("\n ----Current Location---- \n\n","-", current_room.name,"-", "\n\n", textwrap.fill(current_room.description, width=50), "\n\n Items in this Room -> ", current_room_items,"\n\n------------------------" )
   

    # * Waits for user input and decides what to do.

    x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

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

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

    elif (x.lower() == 's'):
        
        try:

            player._set_current_room(current_room.s_to)

        except:

            print("Invalid Room, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

    elif (x.lower() == 'e'):
        
        try:
        
            player._set_current_room(current_room.e_to)

        except:

            print("Invalid Room, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

    elif (x.lower() == 'w'):

        try:

            player._set_current_room(current_room.w_to)

        except:

            print("Invalid Room, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

    elif (x.lower() == 'i'):

        try:

            print("\n Items In This Room Are: \n ")

            if len(current_room.items) == 0:

                print("This room is Empty ")

            else:

                for idx, item in enumerate(current_room.items):
                    
                    print(idx+1, " - Item Name: ", item.name)

            print("\n")

        except:

            print("Error Getting Items, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")

    elif (x.lower() == 'p'):

        try:

            print("\n Items In Player Inventory Are: \n ")

            if len(player.items) == 0:

                print("Your Inventory is Empty ")

            else:

                for idx, item in enumerate(player.items):
                    
                    print(idx+1, " - Item Name: ", item.name)

            print("\n")

        except:

            print("Error Checking Player Inventory")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")
    
    elif (x.lower().strip().split()[0] == 'take'):

        found = False

        item_name = x.lower().strip().split()[1]

        try:

            for item in current_room.items:

                if item.name == item_name:

                    found = True

                    player.items.append(item)

                    new_room_contents = [item for item in current_room.items if item.name != item_name]

                    current_room.items = new_room_contents

                    item.on_take()

            if found == False:

                print(f'\n {item_name} not in the Room')
        
        except:

            print("Error Taking Items, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")


    elif (x.lower().strip().split()[0] == 'drop'):

        found = False

        drop_item_name = x.lower().strip().split()[1]

        try:

            for item in player.items:

                if item.name == drop_item_name:

                    found = True

                    new_list = [item for item in player.items if item.name != drop_item_name]

                    player.set_items(new_list)

                    item.on_drop()

            if found == False:

                    print(f'\n {drop_item_name} not in Player Inventory')

        except:

            print("Error Dropping Items, Try Again")

            x = input("\n ----MENU---- \n N: Travel North \n S: Travel South \n E: Travel East \n W: Travel West \n I: Check Room for Items \n P: Check Players Inventory \n Take [Item]: Take Item \n Drop [Item]: Drop Item \n Q: Quit Game \n\n Enter Your Choice: ")


    elif (x.lower() == 'q'):
        
        quit = True
        
        print("Game Has Been Quit")

    else:

        print("Error Quitting Game")





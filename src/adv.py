from room import Room
from player import Player
from item import Item

## TEST Covers
# Comprehensions
# Classes / Inheritance
# Using a module
# Look for test files
# To pass the sprint challenge, the test files must pass
# Make sure retro is in before lunch

# Declare all items
item = {
    'sword': Item(
        "Sword", 
        "A shabby looking weapon"
    )
}

# Declare all the rooms
room = {
    'outside': Room(
        "Outside Cave Entrance", 
        "North of you, the cave mount beckons",
        []
    ),

    'foyer': Room(
        "Foyer",
        """Dim light filters in from the south. Dusty passages run north and east.""",
        [item['sword']]
    ),

    'overlook': Room(
        "Grand Overlook", 
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
        []
    ),

    'narrow': Room(
        "Narrow Passage", 
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
        []
    ),

    'treasure': Room(
        "Treasure Chamber", 
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
        []
    ),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'],[])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    #
    # * Prints the current room name
    print(f"\n{player.location}\n")
    if len(player.location.items) > 0:
        print("Items in room:")
        for element in player.location.items:
            print(element)
        print("\n")
        
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    command = input("What would you like to do?\n> ").split(' ')
    ## ADD INSTRUCTIONS 
    ## 
    if len(command) > 1: # Action commands
        if command[0] == 'take' or command[0] == 'grab': # Take/Grab item
            # Go through all items in room, check if that item exists, if it does, add it to the bag, if it does not exist, notify
            for item in player.location.items:
                if item.name.lower() == command[1].lower():
                    player.addItem(item)
                    player.location.removeItem(item)

        if command[0] == 'drop':
            for item in player.inventory:
                if item.name.lower() == command[1].lower():
                    player.dropItem(item)
                    player.location.addItem(item)

        if command[0] == 'check' and command[1] == 'bag': # Check bag
            player.checkBag()

    else: # Movement commands
        if command[0] == 'q': # Quit
            break
        elif command[0] == 'n': # Move North
            # check if the player can move to the north
            # if there is, set that north room as the player's location
            #### FIGURE OUT FSTRING THING
            try:
                if player.location.n_to:
                    player.setLocation(player.location.n_to)
            except:
                print("There is no room to your north")
        elif command[0] == 's': # Move South
            try:
                if player.location.s_to:
                    player.setLocation(player.location.s_to)
            except:
                print("There is no room to your south")
        elif command[0] == 'e': # Move East
            try:
                if player.location.e_to:
                    player.setLocation(player.location.e_to)
            except:
                print("There is no room to your east")
        elif command[0] == 'w': # Move West
            try:
                if player.location.w_to:
                    player.setLocation(player.location.w_to)
            except:
                print("There is no room to your west")
        elif command[0] == 'i' or command[0] == 'inventory':
            player.checkBag()

        
        

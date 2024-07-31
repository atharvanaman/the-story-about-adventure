import random

# Define the rooms and items
rooms = {
    'hall': {
        'description': 'You are in a hall with doors to the north, south, east, and west.',
        'exits': ['north', 'south', 'east', 'west']
    },
    'kitchen': {
        'description': 'You are in a kitchen. There\'s a delicious smell, but also something strange.',
        'exits': ['west'],
        'item': 'knife'
    },
    'bedroom': {
        'description': 'You are in a cozy bedroom with a large bed and a wardrobe.',
        'exits': ['east'],
        'item': 'potion'
    },
    'dungeon': {
        'description': 'You are in a dark and damp dungeon. You can feel the presence of something eerie.',
        'exits': ['north'],
        'item': 'key'
    },
    'treasure room': {
        'description': 'You have found the treasure room! But it\'s locked.',
        'exits': ['south'],
        'locked': True
    }
}

# Player's initial state
player_state = {
    'current_room': 'hall',
    'inventory': [],
    'has_key': False,
    'game_over': False
}

# Function to show the current room's description
def describe_room(room_name):
    room = rooms[room_name]
    print(room['description'])
    if 'item' in room:
        print(f"You see a {room['item']} here.")

# Function to handle player movement
def move(direction):
    current_room = player_state['current_room']
    if direction in rooms[current_room]['exits']:
        # Change current room based on direction
        next_room = next((room for room, details in rooms.items() if current_room in details['exits'] and direction in details['exits']), None)
        if next_room:
            player_state['current_room'] = next_room
            print(f"You move {direction} to the {next_room}.")
            describe_room(next_room)
    else:
        print("You can't go that way.")

# Function to pick up items
def take_item(item):
    current_room = player_state['current_room']
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
        player_state['inventory'].append(item)
        print(f"You take the {item}.")
        del rooms[current_room]['item']
        if item == 'key':
            player_state['has_key'] = True
    else:
        print(f"There is no {item} here.")

# Function to check inventory
def check_inventory():
    print("You have:")
    for item in player_state['inventory']:
        print(f"- {item}")

# Function to unlock the treasure room
def unlock_treasure_room():
    if player_state['current_room'] == 'treasure room':
        if player_state['has_key']:
            print("You use the key to unlock the treasure room. You've won the game!")
            player_state['game_over'] = True
        else:
            print("The treasure room is locked. You need a key to open it.")
    else:
        print("You are not at the treasure room.")

# Main game loop
def main():
    print("Welcome to the Adventure Game!")
    describe_room(player_state['current_room'])

    while not player_state['game_over']:
        command = input("\nEnter your action: ").strip().lower()

        if command in ['north', 'south', 'east', 'west']:
            move(command)
        elif command.startswith('take '):
            item = command.split(' ', 1)[1]
            take_item(item)
        elif command == 'inventory':
            check_inventory()
        elif command == 'unlock':
            unlock_treasure_room()
        elif command == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()

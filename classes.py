# classes.py - for all class objects

# ➥ Exit
class Exit:  # exists because we need "north"
    def __init__(self, name: str, room_id: str):
        self.name = name
        self.room_id = room_id
##

# ➥ Item
class Item:
    """
    a class used to represent items
    """
    def __init__(self, item_name: str, item_description: str, item_memory: str, room_id: str, is_invisible: bool):
        """
        Construct a new 'Item' object

        Args:
            item_name (str): name of the item 
            item_description (str): description of the item 
            item_memory (str): memory the item is holding for viewing 
            room_id (str): room the item is held in, changes when dropped 
            is_invisible (bool): if item is displayed in the room's look
        """
        self.name = item_name
        self.description = item_description
        self.memory = item_memory
        self.room_id = room_id
        self.is_invisible = is_invisible

    # for puzzles when we drop items into the "room"
    def set_invisible(self, is_invisible):
        self.is_invisible = is_invisible
##
        
# ➥ Room
class Room:
    def __init__(self, room_id: str, description: str, look: str, exits, is_locked: bool):
        self.room_id = room_id
        self.description = description
        self.exits = exits
        self.look = look
        self.is_locked = is_locked

    # Locks or unlocks room. is_locked is true if locking, and false if unlocking.
    def lock_room(self, is_locked):
        self.is_locked = is_locked

    def set_look(self, look):
        self.look = look

    def set_description(self, description):
        self.description = description
##

# ➥ State
class State:
    def __init__(self, current_room_id: str, visited_rooms: list[str]):
        self.current_room_id = current_room_id
        self.visited_rooms = visited_rooms
        self.inventory = []

    def add_item_inventory(self, item: str):
        self.inventory.append(item)

    def remove_item_inventory(self, item: str):
        self.inventory.remove(item)

    def clear_inventory(self):
        self.inventory.clear()

    def add_visited_room(self, room_id: str):
        self.visited_rooms.append(room_id)
##

# ➥ Puzzle
class Puzzle:
    def __init__(self, puzzle_type: str, room_object: Room, goal_items: list[Item], item_dictionary):
        self.type = puzzle_type
        self.room_object = room_object
        self.goal_items = goal_items
        self.item_dictionary = item_dictionary
##

# ➥ Adventure
class Adventure:
    def __init__(self, room_object_list: list[Room], start_room: str, items: list[Item]):
        self.room_object_list = room_object_list
        self.start_room = start_room
        self.items = items
##

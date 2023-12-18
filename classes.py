# classes.py - for all class objects

# ➥ Exit
class Exit:  # exists because we need "north"
    """
    a class to allow for directional names to our rooms, connects directions such as "north" and "west" with our Kitchen or Throne Room, for example 
    """
    def __init__(self, name: list[str], room_id: str):
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

    # for items in this room, not in your inventory, and aren't invisible
    def viewable(self, current_room_id: str):
        if current_room_id == self.room_id and not self.is_invisible:
            print("--" + self.description)

##
        
# ➥ Room
class Room:
    """a class used to represent our rooms"""
    def __init__(self, room_id: str, description: str, look: str, exits: set['Exit'], is_locked: bool):
        self.room_id = room_id
        self.description = description
        self.exits = exits
        self.look = look
        self.is_locked = is_locked

    # Locks or unlocks room. is_locked is true if locking, and false if unlocking.
    def lock_room(self):
        self.is_locked = True

    def unlock_room(self):
        self.is_locked = False

    def set_look(self, look: str):
        self.look = look

    def set_description(self, description: str):
        self.description = description
##

# ➥ State
class State:
    """the current state of the game """
    def __init__(self, current_room_id: str, visited_rooms: list[str]):
        self.current_room_id = current_room_id
        self.visited_rooms = visited_rooms
        self.inventory = []

    def add_item_inventory(self, item: Item) -> bool:
        # if self.current_room_id == item.room_id and not item.is_invisible:
        # have to decide if we want the player to be able to pick up invisible items
        if self.current_room_id == item.room_id:
            item.room_id = "inventory"
            self.inventory.append(item.name)
            return True
        return False

    def remove_item_inventory(self, item: Item, current_room: str):
        self.inventory.remove(item.name)
        item.room_id = current_room

    def clear_inventory(self):
        self.inventory.clear()

    def add_visited_room(self, room_id: str):
        self.visited_rooms.append(room_id)

    def print_viewable_objects(self, adventure: 'Adventure'):
        for item in adventure.items_object_set: # iterating through item objects
            if item.name not in self.inventory:
                item.viewable(self.current_room_id)

# ➥ Puzzle
class Puzzle:
    """a class used to represent our puzzles. TO-DO: create more puzzles so we can make a universal puzzle class """
    def __init__(self, base_puzzle_description: str, puzzle_room: Room, home_room: Room, goal_room: Room, extra_room_states):
        # self.type = type
        self.base_puzzle_description = base_puzzle_description
        self.puzzle_room = puzzle_room
        self.home_room = home_room
        self.goal_room = goal_room
        self.finished_soup = {"goldfish", "pretzel", "carrot"} # should be universalized JSON file?
        self.current_ingredients = []
        self.extra_room_states = extra_room_states

    def update_description(self):
        room_description = self.base_puzzle_description
        if self.current_ingredients: # does the soup contain anything?
            room_description = f"{self.base_puzzle_description}, {', '.join(self.current_ingredients)}"
        self.puzzle_room.set_description(room_description)
        self.puzzle_room.set_look(room_description)
        self.check_if_finished()

    def add_ingredient(self, ingredient: Item):
        self.current_ingredients.append(ingredient.name)
        ingredient.set_invisible(True)
        self.update_description()
        print(self.puzzle_room.description)
    
    def remove_ingredient(self, ingredient: Item):
        self.current_ingredients.remove(ingredient.name)
        ingredient.set_invisible(False)
        self.update_description()
        print(self.puzzle_room.description)

    # have to universalize this function, thinking using json for defaults
    def check_if_finished(self):
        if self.finished_soup == set(self.current_ingredients): 
            self.home_room.set_description(self.extra_room_states.complete_desc)
            self.home_room.set_look(self.extra_room_states.complete_look)
            print("A warm glowing light is shining from the soup")
            self.goal_room.unlock_room()
        else:
            self.home_room.set_description(self.extra_room_states.incomplete_desc)
            self.home_room.set_look(self.extra_room_states.incomplete_look)
            self.goal_room.lock_room()

##

# ➥ Adventure
class Adventure:
    """a class used to hold all of the rooms and possible items """
    def __init__(self, room_object_set: set[Room], start_room: str, items_object_set: set[Item]):
        self.room_object_set = room_object_set
        self.start_room = start_room
        self.items_object_set = items_object_set
        self.items_name_set = set([item.name for item in items_object_set])
##

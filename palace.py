import json
import re

with open("rooms.json", 'r') as f:
    rooms = json.load(f)

with open("items.json", 'r') as f:
    items = json.load(f)


def strike(text):
    return '\u0336'.join(text)


intro = rooms["story_intro"]
magicIntro = intro.replace("magic", strike("magic"))

greenIntro = re.sub(r"(?P<green>(?<=_)(.*?)(?=,| |,|\'))",
                    r"\033[1;32;40m\g<green>\033[0;37;40m", magicIntro)
coloredIntro = re.sub(r"_", "", greenIntro)

policeReport = rooms["police_report"]
greenPoliceReport = re.sub(r"(?P<green>(?<=_)(.*?)(?=,| |,|\'))",
                           r"\033[1;32;40m\g<green>\033[0;37;40m", policeReport)
redPoliceReport = re.sub(r"(?P<red>(?<=`)(.*?)(?=,| |,|\'))",
                         r"\033[1;31;40m\g<red>\033[0;37;40m", greenPoliceReport)
bluePoliceReport = re.sub(r"(?P<blue>(?<=~)(.*?)(?=,| |,|\'))",
                          r"\033[1;34;40m\g<blue>\033[0;37;40m", redPoliceReport)
coloredPoliceReport = re.sub(r"~|`|_", "", bluePoliceReport)

# Possible Commands
#   go
#   open
#   use (train) (doorbell) <- alias for go
#   approach??
#   compass

# ➥ Exit


class Exit:  # exists because we need "north"
    def __init__(self, name, room_id):
        self.name = name
        self.room_id = room_id
##

# ➥ Item


class Item:
    def __init__(self, item_name, item_description, item_memory, room_id, is_invisible: bool):
        self.name = item_name
        self.description = item_description
        self.memory = item_memory
        self.room_id = room_id
        self.is_invisible = is_invisible

    def set_invisible(self, is_invisible):
        self.is_invisible = is_invisible
##

# ➥ State


class State:
    def __init__(self, current_room, visited_rooms, inventory=[]):
        self.current_room = current_room
        self.visited_rooms = visited_rooms
        self.inventory = inventory

    def add_item_inventory(self, item):
        self.inventory.append(item)

    def remove_item_inventory(self, item):
        self.inventory.remove(item)

    def clear_inventory(self):
        self.inventory.clear()

    def add_visited_room(self, room):
        self.visited_rooms.append(room)
##

# ➥ Room


class Room:
    def __init__(self, room_id, description, look, exits, is_locked: bool):
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

# ➥ Puzzle


class Puzzle:
    def __init__(self, puzzle_type, room_object, goal_items: list, item_dictionary):
        self.type = puzzle_type
        self.room_object = room_object
        self.goal_items = goal_items
        self.item_dictionary = item_dictionary

##

# a.k.a our json reader


def room_list_creator():
    room_object_list = []
    for i in range(len(rooms["rooms"])):
        exit_list = []
        for j in range(len(rooms["rooms"][i]["exits"])):
            exit_list.append(Exit(
                rooms["rooms"][i]["exits"][j]["name"], rooms["rooms"][i]["exits"][j]["room_id"]))
        room_object_list.append(Room(
            rooms["rooms"][i]["id"], rooms["rooms"][i]["description"], rooms["rooms"][i]["look"], exit_list, bool(rooms["rooms"][i]["is_locked"])))
    return room_object_list


def item_list_creator():
    item_list = []
    for i in range(len(items)):
        item_list.append(Item(items[i]["name"], items[i]["description"],
                         items[i]["memory"], items[i]["current_room"], bool(items[i]["is_invisible"])))
    return item_list

# ➥ Adventure


class Adventure:
    def __init__(self, room_object_list=room_list_creator(), start_room=rooms["start_room"], items=item_list_creator()):
        self.room_object_list = room_object_list
        self.start_room = start_room
        self.items = items
##

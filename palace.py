import json

with open("rooms.json", 'r') as f:
    rooms = json.load(f)
    
with open("items.json", 'r') as f:
    items = json.load(f)

# Possible Commands
#   go
#   open
#   use (train) (doorbell) <- alias for go
#   approach??
#   compass

#➥ Exit
class Exit: #exists because we need "north"
    def __init__(self, name, room_id):
        self.name = name
        self.room_id = room_id
##

#➥ Item
class Item:
    def __init__(self, item_name, item_description, item_memory, room_id):
        self.name = item_name
        self.description = item_description
        self.memory = item_memory
        self.room_id = room_id
##

#➥ State
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
##

#➥ Room
class Room:
    def __init__(self, room_id, room_description, look, exits):
        self.room_id = room_id
        self.room_description = room_description
        self.exits = exits
        self.look = look
##

#a.k.a our json reader
def room_list_creator():
    room_object_list = []
    for i in range(len(rooms["rooms"])):
        exit_list = []
        for j in range(len(rooms["rooms"][i]["exits"])):
            exit_list.append(Exit(
                rooms["rooms"][i]["exits"][j]["name"], rooms["rooms"][i]["exits"][j]["room_id"]))
        room_object_list.append(Room(
            rooms["rooms"][i]["id"], rooms["rooms"][i]["description"], rooms["rooms"][i]["look"], exit_list))
    return room_object_list

def room_name_creator():
    room_list = []
    for i in range(len(rooms["rooms"])):
        room_list.append(rooms["rooms"][i]["id"])
    return room_list

def item_list_creator():
    item_list = []
    for i in range(len(items)):
        item_list.append(Item(items[i]["name"], items[i]["description"], items[i]["memory"], items[i]["current_room"]))
    return item_list

#➥ Adventure 
class Adventure:
    def __init__(self, room_name_list=room_name_creator(), room_object_list=room_list_creator(), start_room=rooms["start_room"], items = item_list_creator()):
        self.room_name_list = room_name_list
        self.room_object_list = room_object_list
        self.start_room = start_room
        self.items = items
##

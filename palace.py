import json

class Exit:  
    def __init__(self, name, room_id):
        self._name = name
        self._room_id = room_id 
    
    def get_name(self):
        return self._name
    
    def get_room_id(self):
        return self._room_id

    def set_name(self, new_name):
        self._name = new_name

    def set_room_id(self, new_room_id):
        self._room_id = new_room_id

class Room:
    def __init__(self, room_id, room_description, exits):
        self._room_id = room_id
        self._room_description = room_description
        self._exits = exits
        
    def get_room_id(self):
        return self._room_id

    def get_room_description(self):
        return self._room_description

    def get_exits(self):
        return self._exits

    def set_room_id(self, new_room_id):
        self._room_id = new_room_id

    def set_room_description(self, new_room_description):
        self._room_description = new_room_description

    def set_exits(self, new_exits):
        self._exits = new_exits
        
class Adventure:
    def __init__(self, rooms, starting_room):
        self._rooms = rooms
        self._starting_room = starting_room

    def get_rooms(self):
        return self._rooms
    def get_starting_room(self):
        return self._starting_room

class UnknownRoom(Exception):
    pass

class UnknownExit(Exception):
    pass

def get_exits(room_list, room):
    exits = []
    for i in room_list:
        if i.get_room_id() == room:
            exits = i.get_exits()
    if exits == []:
        raise UnknownRoom
    return exits
def next_room_helper(exit_list, exit):
    room = ""
    for i in exit_list:
        if i.get_name() == exit:
            room = i.get_room_id()
    if room == "":
        raise UnknownExit
    return room

def next_room(adv, room, ex):
    rooms = adv.get_rooms()
    exit_list = get_exits(rooms, room)
    return next_room_helper(exit_list, ex)
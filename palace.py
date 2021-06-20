import json

<<<<<<< HEAD
class Go:
  def __init__(self, exitroom):
    self.exitroom = exitroom
#   goCommand
#   openCommand
#   takeCommand

class State:
  def __init(self, current_room, visited_rooms):
    self.current_room = current_room
    self.visited_rooms = visited_rooms
    
    def get_current(self):
        return self.current_room
    
    def get_visited_rooms(self):
        return self.visited_rooms
    
    def set_current(self, current_room):
        self.current_room = current_room
        
    def set_visited_rooms(self, visited_room):
        self.visited_rooms = visited_room

=======
>>>>>>> e0cd923c8102028a222c0b553a213ff191f27510
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
        
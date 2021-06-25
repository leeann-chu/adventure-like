import json

with open("rooms.json", 'r') as f:
		rooms = json.load(f)

# Possible Commands    
#   goCommand
#   openCommand
#   takeCommand

#➥ Exit
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
##

#➥ State
class State:
	def __init__(self, current_room, visited_rooms):
		self.current_room = current_room
		self.visited_rooms = visited_rooms
	
	def get_current(self):
		return self.current_room

	def get_visited_rooms(self):
		return self.visited_rooms

	def set_current(self, current_room):
		self.current_room = current_room
		
	def set_visited_rooms(self):
		self.visited_rooms.append(self.current_room)
##

#➥ Room
class Room:
	def __init__(self, room_id, room_description, look, exits):
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
##

def room_list_creator():
	room_object_list = []
	for i in range(len(rooms["rooms"])):
		exit_list = []
		for j in range(len(rooms["rooms"][i]["exits"])):
			exit_list.append(Exit(rooms["rooms"][i]["exits"][j]["name"], rooms["rooms"][i]["exits"][j]["room_id"]))
		room_object_list.append(Room(rooms["rooms"][i]["id"], rooms["rooms"][i]["description"], rooms["rooms"][i]["look"], exit_list))
	return room_object_list

def room_name_creator():
	room_list = []       
	for i in range(len(rooms["rooms"])):
		room_list.append(rooms["rooms"][i]["id"])

#➥ Adventure
class Adventure:
	def __init__(self, room_name_list = room_name_creator(), room_object_list = room_list_creator(), start_room = rooms["start_room"]):        
		self.room_name_list = room_name_list
		self.room_object_list = room_object_list
		self.start_room = start_room
  
	def get_room_name_list(self):
			return self.room_name_list

##
			

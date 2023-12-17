# common_utils.py - for all common methods used in game
import json
from classes import  *

# read rooms.json
def readRooms():
    with open("resources/rooms.json", 'r') as f:
        rooms = json.load(f)
    return rooms

# read items.json
def readItems():
    with open("resources/items.json", 'r') as f:
        items = json.load(f)
    return items

def strike(text):
    return '\u0336'.join(text)

# ➥ Get Room
def get_room_object(adventure: Adventure, room_id_input: str):
    room_object_list = [
        room_id for room_id in adventure.room_object_list if room_id.room_id == room_id_input]
    return room_object_list[0]
##

# ➥ Get Item
def get_item_object(adventure: Adventure, item_name_input: str):
    item_object_list = [
        item for item in adventure.items if item.name == item_name_input]
    return item_object_list[0]
##

# a.k.a our json reader
def room_list_creator(rooms: dict):
    """
    Generates all of the rooms in our game using our rooms.json file
    outputs a list of `Rooms`
    """
    room_object_list = []
    for i in range(len(rooms["rooms"])):
        exit_list = []
        for j in range(len(rooms["rooms"][i]["exits"])):
            exit_list.append(Exit(
                rooms["rooms"][i]["exits"][j]["name"], rooms["rooms"][i]["exits"][j]["room_id"]))
        room_object_list.append(Room(
            rooms["rooms"][i]["id"], rooms["rooms"][i]["description"], rooms["rooms"][i]["look"], exit_list, rooms["rooms"][i]["is_locked"]))
    return room_object_list


def item_list_creator(items: list) -> list[Item]:
    item_list = []
    for i in range(len(items)):
        item_list.append(Item(items[i]["name"], items[i]["description"],
                         items[i]["memory"], items[i]["current_room"], bool(items[i]["is_invisible"])))
    return item_list

# ➥ Functions for the puzzles of type 'soup'
def soup_puzzle_complete(puzzle: Puzzle):
    complete = True
    for i in puzzle.goal_items:
        if i.room_id != puzzle.room_object.room_id:
            complete = False
    return complete

def update_descriptions(puzzle: Puzzle):
    for item in puzzle.goal_items:
        if item.room_id == puzzle.room_object.room_id:
            if not item.is_invisible:
                puzzle.room_object.set_description(
                    puzzle.room_object.description + puzzle.item_dictionary.get(item.name))
                puzzle.room_object.set_look(
                    puzzle.room_object.description + puzzle.item_dictionary.get(item.name))
            item.set_invisible(True)
##
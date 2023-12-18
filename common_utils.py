# common_utils.py - for all common methods used in game
import json
import random
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

# ➥ Get Room - converts room_id to a room object
def get_room_object(adventure: Adventure, room_id_input: str) -> Room:
    return next(room for room in adventure.room_object_set if room.room_id == room_id_input)
##

# ➥ Get Item - converts item_name to item object
def get_item_object(adventure: Adventure, item_name_input: str) -> Item:
    return next(item for item in adventure.items_object_set if item.name == item_name_input)
##

# a.k.a our json reader
def room_set_creator(rooms: dict) -> set[Room]:
    """
    Generates all of the rooms in our game using our rooms.json file
    outputs a set of `Rooms`
    """
    room_object_list = []
    for i in range(len(rooms["rooms"])):
        exit_list = []
        for j in range(len(rooms["rooms"][i]["exits"])):
            exit_list.append(Exit(
                rooms["rooms"][i]["exits"][j]["name"], rooms["rooms"][i]["exits"][j]["room_id"]))
        exit_set = set(exit_list)
        room_object_list.append(Room(
            rooms["rooms"][i]["id"], rooms["rooms"][i]["description"], rooms["rooms"][i]["look"], exit_set, rooms["rooms"][i]["is_locked"]))
    room_object_set = set(room_object_list)
    return room_object_set

def item_set_creator(items: list) -> set[Item]:
    item_list = []
    for i in range(len(items)):
        item_list.append(Item(items[i]["name"], items[i]["description"],
                         items[i]["memory"], items[i]["current_room"], bool(items[i]["is_invisible"])))
    item_set = set(item_list)
    return item_set

def drinks_game_logic(input_ingredients: set[str], ingredient_list: set[str], drinks_game: dict) -> str:
    if not input_ingredients.issubset(ingredient_list):
        return "One of your ingredients is dumb and unsanctioned."
    # check if ingredients make a happy meal
    your_masterpiece = drinks_game.get(frozenset(input_ingredients))
    garbage = ["Gunk", "Gak", "Blech"]
    if your_masterpiece:
        return f"You have created {your_masterpiece} \nNice!"
    return f"You have created {random.choice(garbage)}."
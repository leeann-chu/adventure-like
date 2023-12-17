# game_objects.py - for all hardcoded game objects 
from common_utils import *

rooms = readRooms()
items = readItems()

start_room = rooms["start_room"]

state = State(start_room, [start_room])
adventure = Adventure(room_list_creator(rooms), start_room, item_list_creator(items))

# train stuffs
train_stations = ["soup", "debug_room"]

# ➥ Soup Dictionary
SoupDictionary = {
    "carrot": ", carrot",
    "goldfish": ", goldfish",
    "pretzel": ", pretzel"
}
##

# Puzzle(puzzle_type, room_object, goal_items)
SoupPuzzle = Puzzle("soup", get_room_object(adventure, "soup"), [get_item_object(adventure,
    "carrot"), get_item_object(adventure, "goldfish"), get_item_object(adventure, "pretzel")], SoupDictionary)


drink_game = {
    frozenset({"Body Parts", "Herbs", "Water"}): "Tomato Soup - Hmm… this tomato soup looks darker than usual.",
    frozenset({"Meat", "Void", "Stardust"}): "Intergalactic Meatballs - Meatballs from beyond the stars.",
    frozenset({"Fish", "Body Parts", "Bread"}): "FishEye Casserole - Don't make eye contact.",
    frozenset({"Candy", "Meat", "Anger"}): "Despotic Gummy Bears - Revolution!!!",
    frozenset({"Flour", "Eggs", "Butter"}): "Dopamine Flavored Pancakes",
    frozenset({"Void", "Flour", "Water"}): "Bagel Holes - There's nothing there…",
    frozenset({"Critters", "Candy", "Body Parts"}): "Cricket lolly - tastes like chicken",
}

ingredient_list = [
    "Anger",
    "Bread",
    "Body Parts",
    "Butter",
    "Candy",
    "Critters",
    "Eggs",
    "Fish",
    "Flour",
    "Herbs",
    "Meat",
    "Stardust",
    "Void",
    "Water",
]
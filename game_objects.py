# game_objects.py - for all hardcoded game objects 
from collections import namedtuple
from common_utils import *

rooms = readRooms()
items = readItems()

start_room = rooms["start_room"]
confusion = ["Gesundheit!", "Uhhhhhhhh...What?", "Come again?", "Pardon?",
                     "Did your cat walk across your keyboard?", "I don't understand.", "Go fish."]
acquiescence = ["If you say so.", "As you wish.", "Sure.", "Okay.", ":D", "Fine."]

state = State(start_room, [start_room])
adventure = Adventure(room_set_creator(rooms), start_room, item_set_creator(items))

# train stuffs
train_stations = {"soup", "debug_room"}

ExtraRoomStates = namedtuple('ExtraRoomStates', ['incomplete_look', 'complete_look', 'incomplete_desc', 'complete_desc'])
# If we had a different puzzle we'd use a different base description
SoupPuzzle = Puzzle("This soup contains broth", 
    get_room_object(adventure, "soup"), 
    get_room_object(adventure, "kitchen"), 
    get_room_object(adventure, "fridge"),
    ExtraRoomStates(incomplete_look='On the stove, there is a pot of soup cooking and some pasta boiling. The soup appears to be missing some ingredients.',
                    complete_look='On the stove, there is a pot of soup cooking and some pasta boiling. The soup appears to be complete and is glowing with a warm fulfilling light. Yum.',
                    incomplete_desc='You step into what appears to be a kitchen. The room is lit by a hazy yellow light from the appliances, and the smells drifting from the stove and oven remind you of home. \nAll of the cabinets are open except for one, and you can see boxes of sugary cereal and goldfish lining the shelves.',
                    complete_desc='You step into what appears to be a kitchen. The room is lit by a hazy yellow light from the appliances, and the smells drifting from the stove and oven remind you of home. \nAll of the cabinets are open except for one, and you can see boxes of sugary cereal and goldfish lining the shelves. \nOn the stove, there is a pot of soup cooking and some pasta boiling. The soup appears to be complete and is glowing with a warm fulfilling light. Yum. \nThe refrigerator is slightly ajar, and a glowing light is peaking out from the inside.')
)

drinks_game = {
    frozenset({"body parts", "herbs", "water"}): "Tomato Soup - Hmm… this tomato soup looks darker than usual.",
    frozenset({"meat", "void", "stardust"}): "Intergalactic Meatballs - Meatballs from beyond the stars.",
    frozenset({"fish", "body parts", "bread"}): "FishEye Casserole - Don't make eye contact.",
    frozenset({"candy", "meat", "anger"}): "Despotic Gummy Bears - Revolution!!!",
    frozenset({"flour", "eggs", "butter"}): "Dopamine Flavored Pancakes",
    frozenset({"void", "flour", "water"}): "Bagel Holes - There's nothing there…",
    frozenset({"critters", "candy", "body parts"}): "Cricket lolly - tastes like chicken",
}

# only a list because printing purposes, could be turned into anything else, really doesn't matter
ingredient_list = {
    "anger",
    "bread",
    "body parts",
    "butter",
    "candy",
    "critters",
    "eggs",
    "fish",
    "flour",
    "herbs",
    "meat",
    "stardust",
    "void",
    "water",
}
# the description will have the rules on how to play
get_room_object(adventure, "drinks_game").set_look(f"Ingredients: {', '.join(ingredient_list)}")
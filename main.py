import json
import random
from palace import *

adventure = Adventure()
state = State(rooms["start_room"], rooms["start_room"])

#➥ Get Room
def get_room_object(room_id_input):
    room_object_list = [
        room_id for room_id in adventure.room_object_list if room_id.room_id == room_id_input]
    return room_object_list[0]
##
#➥ Get Item
def get_item_object(item_name_input):
    item_object_list = [
        item for item in adventure.items if item.name == item_name_input]
    return item_object_list[0]
##

#➥ Soup Dictionary
SoupDictionary = {
    "carrot" : ", carrot",
    "goldfish" : ", goldfish",
    "pretzel" : ", pretzel"
}
##
# Puzzle(puzzle_type, room_object, goal_items)
SoupPuzzle = Puzzle("soup", get_room_object("soup"), [get_item_object("carrot"), get_item_object("goldfish"), get_item_object("pretzel")], SoupDictionary)

#➥ Functions for the puzzles of type 'soup'
def soup_puzzle_complete(puzzle):
    complete = True
    for i in puzzle.goal_items:
        if i.room_id != puzzle.room_object.room_id:
            complete = False
    return complete

def update_descriptions(puzzle):
    for item in puzzle.goal_items:
        if item.room_id == puzzle.room_object.room_id:
            if not item.is_invisible:
                puzzle.room_object.set_description(puzzle.room_object.description + puzzle.item_dictionary.get(item.name))
                puzzle.room_object.set_look(puzzle.room_object.description + puzzle.item_dictionary.get(item.name))
            item.set_invisible(True)
##

#➥ Parse Command
def parse(inputCommand):
    # go north
    parseInput = inputCommand.lower().split(" ")

    # remove extra spaces
    parseInput_noSpace = [s for s in parseInput if s != '']

    command = parseInput_noSpace.pop(0)

    room_object = get_room_object(state.current_room)

    if command == "go":
        exit_name = " ". join(parseInput_noSpace)
        current_room = state.current_room
        exit_list = room_object.exits

        for exitRoom in exit_list:
            if exit_name in exitRoom.name:  # if we find the exit in the exitRoom name list
                # set exitRoom ID to be our current room
                state.current_room = exitRoom.room_id
                new_room_object = get_room_object(state.current_room)

                # Locked room
                if new_room_object.is_locked:
                    state.current_room = current_room
                    new_room_object = room_object
                    print("This door is locked!")
                    
                if current_room != state.current_room:
                    print(new_room_object.description)
                    
                # Death Screen / Eject Room
                if state.current_room == "ejectRoom":
                    return False

        if current_room != state.current_room:
            for item in adventure.items:
                if state.current_room == item.room_id and item.name not in state.inventory and not item.is_invisible:
                    print("--" + item.description)
                 
        # Room is not recognized
        # if current_room == state.current_room and is_locked_room.is_locked != "True":
        #     print("no")

    elif command == "look":
        print(room_object.look)
        for item in adventure.items:
            if state.current_room == item.room_id and item.name not in state.inventory and not item.is_invisible:
                print("--" + item.description)

    elif command == "take":
        item_name = " ".join(parseInput_noSpace)
        if item_name in state.inventory:
            print("You already have a(n) " + item_name)
        else:
            for item in adventure.items:
                if state.current_room == item.room_id and item_name == item.name and item_name not in state.inventory and not item.is_invisible:
                    state.add_item_inventory(item_name)
                    print("If you say so.")
            if item_name not in state.inventory:
                print("Do 𝘺𝘰𝘶 see a(n) " + item_name + " here?")

    elif command == "drop":
        item_name = " ".join(parseInput_noSpace)
        try:
            state.remove_item_inventory(item_name)
            for item in adventure.items:
                if item.name == item_name:
                    item.room_id = state.current_room
                    # The Soup Puzzle
                    if item in SoupPuzzle.goal_items:
                        update_descriptions(SoupPuzzle)   
                        
            print("If you say so.")
        except ValueError:
            print(item_name + " is not in your inventory!")

    elif command == "inventory":
        for i in state.inventory:
            print("--" + i)

    elif command != "quit" and command != "leave":
        confusion = ["Gesundheit!", "Uhhhhhhhh...What?", "Come again?", "Pardon?", "Did your cat walk across your keyboard?", "I don't understand.", "Go fish."]
        print(random.choice(confusion))

    if soup_puzzle_complete(SoupPuzzle):
        get_room_object("fridge").lock_room(False)
        get_room_object("kitchen").set_look("On the stove, there is a pot of soup cooking and some pasta boiling. The soup appears to be complete. Yum.")
        
    return True
##

# Maybe give option to repeat police_report
print(coloredIntro)
print(coloredPoliceReport)

moved = True
command = ""
while command != "quit" and moved == True:
    command = input("?: ")
    try:
        moved = parse(command)
    except IndexError:
        print("Please input a command :/")

    if command == "leave":
        print("Alright, goodbye then. Have it your way.")
        break
"""
initialize adventure object = this gives the master room list
    = also creates item list

player enters command
parse the command so that it becomes a 
room_exit string

1) ensure room_exit is a proper exit
2) bring player to the next room and print the description
2b) also prints the items in the rooms and their description
3) make sure the look command prints the look part of the room on command
4) add room to visited rooms

"""

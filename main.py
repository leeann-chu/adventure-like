import json
import datetime
import random
from palace import *

#➥ Get Room
def get_room_object(adventure, state):
    room_object_list = [
        room_id for room_id in adventure.room_object_list if room_id.room_id == state.current_room]
    return room_object_list[0]
##

#➥ Parse Command
def parse(inputCommand):
    # go north
    parseInput = inputCommand.lower().split(" ")

    # remove extra spaces
    parseInput_noSpace = [s for s in parseInput if s != '']

    command = parseInput_noSpace.pop(0)

    room_object = get_room_object(adventure, state)

    if command == "go":
        exit_name = " ". join(parseInput_noSpace)
        current_room = state.current_room
        exit_list = room_object.exits

        for exitRoom in exit_list:
            if exit_name in exitRoom.name:  # if we find the exit in the exitRoom name list
                # set exitRoom ID to be our current room
                state.current_room = exitRoom.room_id
                new_room_object = get_room_object(adventure, state)
                # Death Screen
                if state.current_room == "ejectRoom":
                    print(new_room_object.room_description)
                    return False
                print(new_room_object.room_description)
        if current_room != state.current_room:
            for item in adventure.items:
                if state.current_room == item.room_id and item.name not in state.inventory:
                    print(item.description)

        if current_room == state.current_room:
            print("no")

    elif command == "look":
        print(room_object.look)
        for item in adventure.items:
            if state.current_room == item.room_id and item.name not in state.inventory:
                print(item.description)

    elif command == "take":
        item_name = " ". join(parseInput_noSpace)
        if item_name in state.inventory:
            print("You already have a(n) " + item_name)
        else:
            for item in adventure.items:
                if state.current_room == item.room_id and item_name == item.name and item_name not in state.inventory:
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
            print("If you say so.")
        except ValueError:
            print(item_name + " is not in your inventory!")

    elif command == "inventory":
        for i in state.inventory:
            print("--" + i)

    elif command != "quit" and command != "leave":
        confusion = ["Gazuntite!", "Uhhhhhhhh...What?", "Come again?", "Pardon?", "Did your cat walk accross your keyboard?", "I don't understand.", "Go fish."]
        print(random.choice(confusion))
    return True
##

with open("story.json", 'r') as f:
    story = json.load(f)

def strike(text):
    return '\u0336'.join(text)

intro = story["story_intro"]
format_intro = intro.replace("magic", strike("magic"))

# Maybe give option to repeat police_report
print(format_intro)
print(story["police_report"])

adventure = Adventure()

state = State(rooms["start_room"], rooms["start_room"])

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

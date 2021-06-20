import json
import datetime
from palace import *

#➥ Parse Command  
def parse(inputCommand):
    # go north
    parseInput = inputCommand.lower().split(" ")
    
    # remove extra spaces
    parseInput_noSpace = [s for s in parseInput if s != '']
    
    if parseInput_noSpace.pop(0) == "go":
        # make sure 'north' is a proper exit
        exit_name = " ". join(parseInput_noSpace)
        print("current room:" + state.current_room)
        print("room name list" + adventure.room_name_list)
        if state.current_room in adventure.room_name_list:
   
            name_index = adventure.room_name_list.index(state.current_room)
            room_object = adventure.room_object_list[name_index]
            
            for i in room_object.exits:
                if exit_name in i:
                    print("found exit_name")
                    return True
                else:
                    return False
        else:
            print("no")
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

command = ""
while command != "quit":
    
    command = input("?: ")
    parse(command)
    
    if command == "leave":
        print("Alright, goodbye then. Have it your way.")
        break	 
"""
initialize adventure object = this gives the master room list

player enters command
parse the command so that it becomes a 
room_exit string

1) ensure room_exit is a proper exit
2) bring player to the next room and print the description
3) make sure the look command prints the look part of the room on command
4) add room to visited rooms

"""

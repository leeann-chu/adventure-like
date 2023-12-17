# main.py
import re
from parse import *

rooms = readRooms() # readRooms is directly from a json

# ➥ Starting up the game 
intro = rooms["story_intro"]
magicIntro = intro.replace("magic", strike("magic"))

greenIntro = re.sub(r"(?P<green>(?<=_)(.*?)(?=,| |,|\'))",
                    r"\033[1;32;40m\g<green>\033[0;37;40m", magicIntro)
decoratedIntro = re.sub(r"_", "", greenIntro)

policeReport = rooms["police_report"]
greenPoliceReport = re.sub(r"(?P<green>(?<=_)(.*?)(?=,| |,|\'))",
                        r"\033[1;32;40m\g<green>\033[0;37;40m", policeReport)
redPoliceReport = re.sub(r"(?P<red>(?<=`)(.*?)(?=,| |,|\'))",
                        r"\033[1;31;40m\g<red>\033[0;37;40m", greenPoliceReport)
bluePoliceReport = re.sub(r"(?P<blue>(?<=~)(.*?)(?=,| |,|\'))",
                        r"\033[1;34;40m\g<blue>\033[0;37;40m", redPoliceReport)
decoratedPoliceReport = re.sub(r"~|`|_", "", bluePoliceReport)
##

# Maybe give option to repeat police_report
print(decoratedIntro)
print(decoratedPoliceReport)

command = ""
moved = True
while command != "quit" and moved == True:
    command = input("?: ")
    try:
        moved = parse(command)
    except IndexError:
        print("Please input a command :/")

    if command == "leave" or command == "exit":
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
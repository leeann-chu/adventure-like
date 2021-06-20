import json
import datetime
from palace import *
  
def parse(inputCommand):
  parseInput = inputCommand.split(" ")
  parseInput_noSpace = [s for s in parseInput if s != '']
  if parseInput_noSpace.pop(0):
    room = Go(parseInput_noSpace)
    return room.exitroom

with open("rooms.json", 'r') as f:
  story = json.load(f)
  
def strike(text):
    return '\u0336'.join(text)

intro = story["story_intro"]
format_intro = intro.replace("magic", strike("magic"))

print(format_intro)
print(story["police_report"])

command = ""
while command != "quit":
  command = input("?: ")
  parse(command)
  
  if command == "look":
    print(story["abyss_look"])
    
  if command == "leave":
    print("Alright, goodbye then. Have it your way.")
    break
    
    
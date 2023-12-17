# parse.py - for parsing main game loop
import random
from game_objects import *

# Possible Commands
#   go
#   open
#   use (train) (doorbell) <- alias for go
#   approach??
#   compass / map (tells directions and name of current room)

# ➥ Parse Command
def parse(inputCommand):
    # go north
    parseInput = inputCommand.lower().split(" ")

    # remove extra spaces
    parseInput_noSpace = [s for s in parseInput if s != '']

    command = parseInput_noSpace.pop(0)

    room_object = get_room_object(adventure, state.current_room_id)

    if command == "go":
        exit_name = " ". join(parseInput_noSpace)
        current_room_id = state.current_room_id
        exit_list = room_object.exits

        for exitRoom in exit_list:
            if exit_name in exitRoom.name:  # if we find the exit in the exitRoom name list
                # set exitRoom ID to be our current room
                state.current_room_id = exitRoom.room_id
                new_room_object = get_room_object(adventure, state.current_room_id)

                # TO-DO: Move locked to common_utils
                # Locked room
                if new_room_object.is_locked:
                    print("our room is locked")
                    state.current_room_id = current_room_id
                    new_room_object = room_object
                    print("This door is locked!")

                # if we're in the train room 
                if current_room_id == "train":
                    if state.current_room_id not in state.visited_rooms:
                        state.current_room_id = current_room_id
                        new_room_object = room_object
                    else:
                        if state.current_room_id in train_stations:
                            print("You step into the train and hear a mighty chuff as the pistons engage, and the wheels start turning. The train whisks you away on tracks that fill themselves in as you go.")
                
                # Actual movement to a new room
                if current_room_id != state.current_room_id:
                    print(new_room_object.description)
                    if state.current_room_id not in state.visited_rooms:
                        state.add_visited_room(state.current_room_id)
                        if state.current_room_id in train_stations:
                            train = get_room_object(adventure, "train")
                            train.set_look(train.look + "\n---" + state.current_room_id)

                # Death Screen / Eject Room
                if state.current_room_id == "ejectRoom":
                    return False

        # print list of items in the room
        if current_room_id != state.current_room_id:
            for item in adventure.items:
                if state.current_room_id == item.room_id and item.name not in state.inventory and not item.is_invisible:
                    print("--" + item.description)

        # Room is not recognized
        # if current_room_id == state.current_room_id and is_locked_room.is_locked != "True":
        #     print("no")

    elif command == "look":
        print(room_object.look)
        for item in adventure.items:
            if state.current_room_id == item.room_id and item.name not in state.inventory and not item.is_invisible:
                print("--" + item.description)

    elif command == "take":
        item_name = " ".join(parseInput_noSpace)
        if item_name in state.inventory:
            print("You already have a(n) " + item_name)
        else:
            for item in adventure.items:
                if state.current_room_id == item.room_id and item_name == item.name and item_name not in state.inventory and not item.is_invisible:
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
                    item.room_id = state.current_room_id
                    # The Soup Puzzle
                    if item in SoupPuzzle.goal_items:
                        update_descriptions(SoupPuzzle)

            print("If you say so.")
        except ValueError:
            print(item_name + " is not in your inventory!")

    elif command == "inventory":
        for i in state.inventory:
            print("--" + i)

    elif command != "quit" and command != "leave" and command !="exit":
        confusion = ["Gesundheit!", "Uhhhhhhhh...What?", "Come again?", "Pardon?",
                     "Did your cat walk across your keyboard?", "I don't understand.", "Go fish."]
        print(random.choice(confusion))

    # TO-DO: move function to SoupClass (this only needs to fire once)
    if soup_puzzle_complete(SoupPuzzle):
        get_room_object(adventure, "fridge").lock_room(False) # unlock the fridge
        get_room_object(adventure, "kitchen").set_look(
            "On the stove, there is a pot of soup cooking and some pasta boiling. The soup appears to be complete. Yum.")

    return True
##
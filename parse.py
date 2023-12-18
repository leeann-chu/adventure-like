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
    command = parseInput_noSpace.pop(0) # remove first command
    target_name = " ".join(parseInput_noSpace) # go <- command kitchen <- target name

    room_object = get_room_object(adventure, state.current_room_id)

    if command == "go":
        current_room_id = state.current_room_id

        # loops thorugh all room_objects in our exit list
        for exit_object in room_object.exits:
            if target_name in exit_object.name: # names are the possible names for exit rooms 
                # set exitRoom ID to be our current room
                state.current_room_id = exit_object.room_id
                new_room_object = get_room_object(adventure, state.current_room_id)

                # TO-DO: Move locked to common_utils
                # Locked room
                if new_room_object.is_locked:
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
            state.print_viewable_objects(adventure)

        # Room is not recognized
        # if current_room_id == state.current_room_id and is_locked_room.is_locked != "True":
        #     print("no")

    elif command == "look":
        print(room_object.look)
        state.print_viewable_objects(adventure)

    elif command == "take": 
        if target_name in state.inventory: # you already have it
            print(f"You already have {target_name}. Don't be greedy.")
            # need to use get_item_object() twice so it doesn't error not found
        elif target_name in adventure.items_name_set and state.add_item_inventory(get_item_object(adventure, target_name)):
            print(random.choice(acquiescence)) # okay you can take it fine   
            # The Soup Puzzle - take
            if state.current_room_id == "soup" and target_name in SoupPuzzle.finished_soup:
                SoupPuzzle.remove_ingredient(get_item_object(adventure, target_name))  
        else:
            print(f"Do 𝘺𝘰𝘶 see {target_name} here?")        

    elif command == "drop": # if it's in your inv drop it. otherwise complain
        if target_name not in state.inventory:
            print(f"{target_name} is not in your inventory!")
            # need to use get_item_object() twice so it doesn't error not found
        else:
            state.remove_item_inventory(get_item_object(adventure, target_name), state.current_room_id)
            print(random.choice(acquiescence)) 
            # The Soup Puzzle - drop
            if state.current_room_id == "soup" and target_name in SoupPuzzle.finished_soup:
                SoupPuzzle.add_ingredient(get_item_object(adventure, target_name))

    elif command =="mix" and state.current_room_id == "drinks_game":
        if len(target_name.split(", ")) == 3:
            print(drinks_game_logic(set(target_name.split(", ")), ingredient_list, drinks_game))
        else:
            print("You must use exactly three ingredients to create a(n) masterpiece!")

    elif command == "inventory":
        for i in state.inventory:
            print("--" + i)

    elif command != "quit" and command != "leave" and command !="exit":
        print(random.choice(confusion))
        
    return True
##
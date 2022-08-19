"""
The helper_function module contains functions that are used to
process the user input while the program is running
"""
import pickle
import os
import time
import sys
from PIL import Image
from global_data import string_responses, dashing, dash_objectives



def get_map(map_location):
    """
    Get map retuns the map path based on the users current map location
    """
    return f'PythonPeasantQuest\\images\\{map_location}.png'


def enter_is_terminate(key_code):
    """
    enter_is_terminate returns the code for Ctrl+G when the enter key is hit
    """
    if key_code == 10:
        key_code = 7
    return key_code


def look_item(subwin,txtwin, location):
    """
    look_item presents the user with a description string
    the string returned is pulled from dash_objectives and is one of two things
    1. a description of the items available in the area
    2. a prompt that there's nothing left to see and to move on
    """
    item_count = 0
    item_key = dash_objectives.objectiveDict[location]["items"]
    print_string = ""
    if item_key:
        for item in item_key:
            description = item_key[item]["description"]
            if item_count == 0:
                print_string+=f"You look and see {description}"
                item_count += 1
            else:
                print_string+=f" and {description}\n"
        print_string += "What do you do ??:"
        sub_refresh(subwin,txtwin,print_string,location)
    else:
        sub_refresh(subwin,txtwin,string_responses["objCompleteLook"],location)


def get_item(subwin,txtwin,location,item):
    """
    get_item allows the user to get the available item
    this get can only be done if the user has the prerequisites
    if the user does not have the prerequisites they are returned the
    noprereqs string and the item is not appended to their inventory
    """
    item_objv = dash_objectives.objectiveDict[location]["items"]

    if item in item_objv and item not in dashing.inventory:
        prereqs = item_objv[item]["prereqs"]
        if (prereqs != "None" and prereqs in dashing.inventory) or (prereqs == "None"):
            response = item_objv[item]["get"]
            del item_objv[item]
            dashing.inventory.append(item)
        else:
            response = item_objv[item]["noprereqs"]
        sub_refresh(subwin,txtwin,response,location)

        #Checking that the items for trogdor win conditions are present and updating accordingly
        if "belt" in dashing.inventory:
            dashing.stink = True
        if "robe" in dashing.inventory:
            dashing.dress = True
        if "lantern" in dashing.inventory:
            dashing.fire = True


    else:
        response = "You can't get that, What do you do ??:"
        sub_refresh(subwin,txtwin,response,location)


def sub_refresh(subwin, txtwin, witty_response, location):
    """
    sub_refresh is a middle function that refreshes the text box
    """
    subwin.clear()
    subwin.refresh()
    text_interact(subwin, txtwin, witty_response, location)


def text_interact(subwin, txtwin, witty_response, location):
    """
    text_interact is used to do the following
    1. start the text box
    2. capture user entry
    3. call the appropriate function based on user entry
    """
    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather()
    cont_interim = contents.split("??:", 1)[1]
    cont_res = "".join(cont_interim).strip().lower()

    if cont_res == "map":
        if "map" in dashing.inventory:
            with Image.open(get_map(location)) as img:
                img.show()
            sub_refresh(subwin,txtwin,string_responses["mapResponse"],location)
        else:
            sub_refresh(subwin,txtwin,string_responses["dontGotIt"],location)

    elif cont_res == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        sub_refresh(subwin,txtwin,inv,location)

    elif "look" in cont_res:
        look_item(subwin,txtwin, location)

    elif "get" in cont_res:
        get_item(subwin,txtwin,location,cont_res[4:])

    elif cont_res == "help":
        sub_refresh(subwin,txtwin,string_responses["simpleInstructions"], location)

    elif cont_res == "done":
        pass
    elif cont_res == "save":
        with open('PythonPeasantQuest/peasant_data.pkl', 'wb') as outp:
            pickle.dump(dashing,outp,pickle.HIGHEST_PROTOCOL)
        sub_refresh(subwin,txtwin,string_responses["saveSuccess"],location)
    else:
        sub_refresh(subwin,txtwin,string_responses["jerkResponse"], location)

def load_animation(strAnimate):
    """
    The load animation displays an animated string to the user
    """
    os.system("clear")

    #Referenced from Geeks for Geeks
    load_str = strAnimate
    ls_len = len(load_str)

    animation = "|/-\\"
    anicount = 0

    counttime = 0
    i = 0

    while(counttime != 50):
        time.sleep(.075)
        load_str_list = list(load_str)
        x=ord(load_str_list[i])
        y=0

        if x != 32 and x != 46:    
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)

        res =''
        for j in range(ls_len):
            res = res + load_str_list[j]

        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()

        load_str = res
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

    #Once timer is up it clears the terminal and shows the next area
    os.system("clear")
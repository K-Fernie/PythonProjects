"""
The helper_function module contains functions that are used to
process the user input while the program is running
"""
import pickle
from global_data import string_responses, dashing, dash_objectives
from PIL import Image

"""
Get map retuns the map path based on the users current map location
"""
def get_map(map_location):
    return f'PythonPeasantQuest\images\{map_location}.png'

"""
enter_is_terminate returns the code for Ctrl+G when the enter key is hit
"""
def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

"""
look_item presents the user with a description string
the string returned is pulled from dash_objectives and is one of two things
1. a description of the items available in the area
2. a prompt that there's nothing left to see and to move on
"""
def look_item(subwin,txtwin, location):
    itemCount = 0
    itemKey = dash_objectives.objectiveDict[location]["items"]
    printstring = ""
    if itemKey:
        for item in itemKey:
            description = itemKey[item]["description"]
            if itemCount == 0:
                printstring+=f"You look and see {description}"
                itemCount += 1
            else:
                printstring+=f" and {description}\n"
        printstring += "What do you do ??:"
        sub_refresh(subwin,txtwin,printstring,location)
    else:
        sub_refresh(subwin,txtwin,string_responses["objCompleteLook"],location)

"""
get_item allows the user to get the available item
this get can only be done if the user has the prerequisites
if the user does not have the prerequisites they are returned the 
noprereqs string and the item is not appended to their inventory
"""
def get_item(subwin,txtwin,location,item):
    itemObj = dash_objectives.objectiveDict[location]["items"]

    if item in itemObj and item not in dashing.inventory:
        prereqs = itemObj[item]["prereqs"]
        if (prereqs != "None" and prereqs in dashing.inventory) or (prereqs == "None"):
            response = itemObj[item]["get"]
            del itemObj[item]
            dashing.inventory.append(item)
        else:
            response = itemObj[item]["noprereqs"]
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

"""
sub_refresh is a middle function that refreshes the text box
"""
def sub_refresh(subwin, txtwin, witty_response, location):
    subwin.clear()
    subwin.refresh()
    text_interact(subwin, txtwin, witty_response, location)

"""
text_interact is used to do the following
1. start the text box
2. capture user entry
3. call the appropriate function based on user entry
"""
def text_interact(subwin, txtwin, witty_response, location):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather()
    contInterim = contents.split("??:", 1)[1]
    contRes = "".join(contInterim).strip().lower()

    if contRes == "map":
        if "map" in dashing.inventory:
            with Image.open(get_map(location)) as img:
                img.show()
            sub_refresh(subwin,txtwin,string_responses["mapResponse"],location)
        else:
            sub_refresh(subwin,txtwin,string_responses["dontGotIt"],location)

    elif contRes == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        sub_refresh(subwin,txtwin,inv,location)

    elif "look" in contRes:
        look_item(subwin,txtwin, location)

    elif "get" in contRes:
        get_item(subwin,txtwin,location,contRes[4:])

    elif contRes == "help":
        sub_refresh(subwin,txtwin,string_responses["simpleInstructions"], location)

    elif contRes == "done":
        pass
    elif contRes == "save":
        with open('PythonPeasantQuest/peasant_data.pkl', 'wb') as outp:
            pickle.dump(dashing,outp,pickle.HIGHEST_PROTOCOL)
        sub_refresh(subwin,txtwin,string_responses["saveSuccess"],location)
    else:
        sub_refresh(subwin,txtwin,string_responses["jerkResponse"], location)

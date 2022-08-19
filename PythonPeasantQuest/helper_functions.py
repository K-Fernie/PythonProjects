import pickle
from global_data import string_responses, dashing, dash_objectives
from PIL import Image


def getMap(map_location):
    return f'PythonPeasantQuest\images\{map_location}.png'

def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

def lookItem(subwin,txtwin, location):
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
        subRefresh(subwin,txtwin,printstring,location)
    else: 
        subRefresh(subwin,txtwin,string_responses["objCompleteLook"],location)

def getItem(subwin,txtwin,location,item):
    itemObj = dash_objectives.objectiveDict[location]["items"]

    if item in itemObj and item not in dashing.inventory:
        prereqs = itemObj[item]["prereqs"]
        if (prereqs != "None" and prereqs in dashing.inventory) or (prereqs == "None"):
            response = itemObj[item]["get"]
            del itemObj[item]
            dashing.inventory.append(item)
        else: 
            response = itemObj[item]["noprereqs"]
        subRefresh(subwin,txtwin,response,location)

        #Checking that the items for trogdor win conditions are present and updating accordingly
        if "belt" in dashing.inventory: 
            dashing.stink = True
        if "robe" in dashing.inventory:
            dashing.dress = True
        if "lantern" in dashing.inventory:
            dashing.fire = True
        

    else: 
        response = "You can't get that, What do you do ??:"
        subRefresh(subwin,txtwin,response,location)


def subRefresh(subwin, txtwin, witty_response, location):
    subwin.clear()
    subwin.refresh()
    textInteract(subwin, txtwin, witty_response, location)


def textInteract(subwin, txtwin, witty_response, location):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather()
    contInterim = contents.split("??:", 1)[1]
    contRes = "".join(contInterim).strip().lower()
    
    if contRes == "map":
        if "map" in dashing.inventory:
            with Image.open(getMap(location)) as img: 
                img.show()
            subRefresh(subwin,txtwin,string_responses["mapResponse"],location)
        else:
            subRefresh(subwin,txtwin,string_responses["dontGotIt"],location)

    elif contRes == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        subRefresh(subwin,txtwin,inv,location)

    elif "look" in contRes:
        lookItem(subwin,txtwin, location)

    elif "get" in contRes:
        getItem(subwin,txtwin,location,contRes[4:])

    elif contRes == "help": 
        subRefresh(subwin,txtwin,string_responses["simpleInstructions"], location)

    elif contRes == "done":
        pass
    elif contRes == "save":
        with open('PythonPeasantQuest/peasant_data.pkl', 'wb') as outp:
            pickle.dump(dashing,outp,pickle.HIGHEST_PROTOCOL)
        subRefresh(subwin,txtwin,string_responses["saveSuccess"],location)
    else: 
        subRefresh(subwin,txtwin,string_responses["jerkResponse"], location)


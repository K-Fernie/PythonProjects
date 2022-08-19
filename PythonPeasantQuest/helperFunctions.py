import curses
from re import sub
from globalInfo import stringResponses, getMap, dashObjectives, dashing
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import contains, truediv
from travelAnimation import load_animation
from Peasant import Peasant
from PIL import Image

def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

def lookItem(subwin,txtwin, location):
    itemCount = 0
    itemKey = dashObjectives.objectiveDict[location]["items"]
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
        subRefresh(subwin,txtwin,stringResponses["objCompleteLook"],location)

def getItem(subwin,txtwin,location,item):
    itemObj = dashObjectives.objectiveDict[location]["items"]

    if item in itemObj and item not in dashing.inventory:
        prereqs = itemObj[item]["prereqs"]
        if (prereqs != "None" and prereqs in dashing.inventory) or (prereqs == "None"):
            response = itemObj[item]["get"]
            del itemObj[item]
            dashing.inventory.append(item)
        else: 
            response = itemObj[item]["noprereqs"]
        subRefresh(subwin,txtwin,response,location)

        #Checking that the items for trogdor win conditions are present
        if "belt" in dashing.inventory: 
            dashing.stink = True
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
    contents = txtwin.gather().split("??:", 1)[1]
    contRes = "".join(contents).strip().lower()
    

    if contRes == "map":
        if "map" in dashing.inventory:
            with Image.open(getMap(location)) as img: 
                img.show()
            subRefresh(subwin,txtwin,stringResponses["mapResponse"],location)
        else:
            subRefresh(subwin,txtwin,stringResponses["dontGotIt"],location)
    elif contRes == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        subRefresh(subwin,txtwin,inv,location)

    elif "look" in contRes:
        lookItem(subwin,txtwin, location)

    elif "get" in contRes:
        getItem(subwin,txtwin,location,contRes[4:])

    elif contRes == "help": 
        subRefresh(subwin,txtwin,stringResponses["simpleInstructions"], location)

    elif contRes == "done":
        pass
    elif contRes == "save":
        #TODO - pass a timestamp, and the peasant information to a save file
        pass
    else: 
        subRefresh(subwin,txtwin,stringResponses["jerkResponse"], location)


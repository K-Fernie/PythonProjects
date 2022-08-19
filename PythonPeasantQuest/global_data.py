import json
import copy
from peasant_classes import Peasant, Objectives

def string_response(string):
    string_responses = {
            
            "complexInstructions" : "1.You will do many things in text mode press the 'home' key to enter text mode\n"\
                "2.Type 'done' and press enter to exit text mode\n"\
                "3 Use the arrow keys to move around\n"\
                "4 If you get lost you can always type 'help'\n"\
                "5. When entering an area type 'look' for some informations\n"\
                "6. To get an item type 'get <item>'\n"\
                "7. Type 'inv' for a list of your stuff\n"\
                "8. In an attack situation type 'attack'\n"   
                "9. If you are lost type 'map' just for a simple .jpeg (this isn't ubisoft games!)\n"\
                "10. Don't get BuRnEnAtEd",
        
            "simpleInstructions" : "1. You need to DRESS, STINK, and be on FIRE like a peasant"\
                "2. When entering an area type 'look' for some informations"\
                "3. To get an item type 'get <item>'\n"\
                "4. Type 'inventory' for a list of your stuff\n"\
                "5. Type 'map' for your map\n"\
                "What do you do ??:",
            
            "introText": "\nYou are Rather Dashing, a humble peasant living in the peasant kingdom of Peasantry\n" \
                "You return home from a vacation on Scalding Lake only to find that Trogdor the Burninator\n" \
                "has burninated your thatched roof cottage along with all your goods and services.\n" \
                "With nothing left to lose you swear you will destroy that Wingaling.\n"\
                "You must ready yourself to head east towards the mountain atop which Trogdor lives.",
            
            "outline":"Welcome to your quest to defeat Trogdor the burninator\n"\
                "Before you can go and defeat that TrogDORK you are going to need a few things\n"\
                "Right now you are far too clean, you will need to find items to become a true peasant\n"\
                "You first need to STINK like a peasant\n"\
                "Next you need to DRESS like a peasant\n"\
                "Last you need to be on FIRE like a peasant\n"\
                "Only then will you be ready for VENGANCE",

            "screenInitText": "Type 'done' to exit text mode\nWhat do you want poor peasant??: ", 

            "objCompleteLook": "You've seen all you need to see here\nGet Moving on your quest!!\nWhat do you do ??: ",

            "jerkResponse":"You would like to get that wouldn't you ??: ",

            "gotIt":"You already have that item dingus\n What do you do ??:",

            "dontGotIt":"You don't have that item dingus\n What do you do ??:",

            "mapResponse":"Now that you know where you are....\nWhat do you do ??:",

            "playAgain": "Would you like to play again y/n ??:",

            "saveSuccess":"Your game has been successfully saved to the single save\nslot!\nWhat do you do ??:"

    }
    return string_responses[string]

"""
Created a global variable bank to be initialized on start
Placed here to ensure no circular imports occur
"""
global dashing
dashing = Peasant("B3", [], False, False, False)

with open('PythonPeasantQuest\mapObjectives.json', 'r') as objective_file:
    map_objectives = json.load(objective_file)

dash_objectives = Objectives(map_objectives)
dash_objectives_copy = copy.deepcopy(map_objectives)


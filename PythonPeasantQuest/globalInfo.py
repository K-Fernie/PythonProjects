import json
from Peasant import Peasant

global stringResponses 
stringResponses = {
        
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
        
        "riddles":{
            "To whom did the robe you're wearing originally belong?" : "Naked Ned", 
            "What color are the leaves on the tree that grows by the well?": "Orange", 
            "What did you win from the Archery game?": "SuperTimeFunBow", 
            "What does Mendelev have to tell Dongolev?": "Haldo", 
            "What is the only creature the Johnka fears?": "The Kerrek", 
            "What was the Innkeeper's pantry full of?": "Old Man Rub", 
            "Which one of these letters is the letter C?": "C", 
            "What is the land speed of a North American Swallow?": "Coconut Shell"
            },

        "screenInitText": "Type 'done' to exit text mode\nWhat do you want poor peasant??: ", 

        "objCompleteLook": "You've seen all you need to see here\nGet Moving on your quest!!\nWhat do you do ??: ",

        "jerkResponse":"You would like to get that wouldn't you ??: ",

        "gotIt":"You already have that item dingus\n What do you do ??:",

        "dontGotIt":"You don't have that item dingus\n What do you do ??:",

        "mapResponse":"Now that you know where you are....\nWhat do you do ??:",

}

global getMap
def getMap(mapLocation):
    return f'PythonPeasantQuest\images\{mapLocation}.png'

global dashing
dashing = Peasant("Dashing", "B3", [], False, False, False)

global mapObjectives
with open('PythonPeasantQuest\mapObjectives.json', 'r') as objectiveFile:
    mapObjectives = json.load(objectiveFile)
          
from art import *
import os
from travelAnimation import load_animation
from A4 import peasantHome


#Game starts - describes character
#HELP: when typed at any point shows certain commands
#MoveTo: Allows the character to move to a certain point on the map
#Each LOCATION: has certain objectives (that allow the story to progress)
#Hero has items that they must obtain, if item == true then they can do a certain action


def main():
    

    tprint("PeasCant Quest", font="epic",chr_ignore=True)
    print("GENERAL INSTRUCTIONS\n")
    print("-Use the arrow keys to move around")
    print("-Type 'm' at any time to access the map")

    startGame = input("Are you ready to begin the quest?? y/n: ")
    #create a gameinit(startGame) function that is called and all the rest of the progress goes from here
     
    if startGame.lower() == "y":
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print("\nYou are Rather Dashing, a humble peasant living in the peasant kingdom of Peasantry\n"
        + "You return home from a vacation on Scalding Lake only to find that Trogdor the Burninator " +
        "has burninated your thatched roof cottage along with all your goods and services.\n" + 
        "With nothing left to lose, you swear to get revenge on that Wingaling Dragon in the name of burninated peasants everywhere.\n" + 
        "You head east towards the mountain atop which NOTTrogdor lives.")
        mv = input("\nPress ENTER to BEGIN\n")
        if(mv.lower() != "q"):
            os.system("clear")
            peasantHome()
            
    else: 
        print("Come back again... if you are peasanty enough!!")
    #TODO - Create a scene change function that shows animation for scene change
    #TODO - Figure out if theres a way to clear the command line
    #TODO - Create different Scenes with objectives. The player will have scene objectives listed in his class and the scene will search for it's objective to determine if the scene is complete

if __name__ == "__main__":
    main()
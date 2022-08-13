from art import *
import os
from travelAnimation import load_animation
from A4 import peasantHome
from globalInfo import complexInstructions

#Game starts - describes character
#HELP: when typed at any point shows certain commands
#MoveTo: Allows the character to move to a certain point on the map
#Each LOCATION: has certain objectives (that allow the story to progress)
#Hero has items that they must obtain, if item == true then they can do a certain action


def main():

    tprint("PeasCant Quest", font="epic",chr_ignore=True)
    print(complexInstructions)
    

    startGame = input("Are you ready to begin the quest?? y/n: ")
     
    if startGame.lower() == "y":
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print("\nYou are Rather Dashing, a humble peasant living in the peasant kingdom of Peasantry\n" \
                "You return home from a vacation on Scalding Lake only to find that Trogdor the Burninator\n" \
                "has burninated your thatched roof cottage along with all your goods and services.\n"   
                "With nothing left to lose, you swear to get revenge on that Wingaling Dragon\n"  
                "You must ready yourself to head east towards the mountain atop which Trogdor lives.")
                
        mv = input("\nPress ENTER to BEGIN\n")
        if(mv.lower() != "q"):
            os.system("clear")
            load_animation("Awaaaay we goooo....")
            #TODO - uncomment this  code when you are ready to test, right now building out the bones
            #peasantHome()
            
    else: 
        print("Come back again... if you are peasanty enough!!")

if __name__ == "__main__":
    main()
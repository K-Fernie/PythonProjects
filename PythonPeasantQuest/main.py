import os
import pickle
from art import tprint, aprint
from travelAnimation import load_animation
from gameStart import gameStart
from globalData import stringResponses, dashing


"""Main function to be executed at runtime"""
def main():
    """
    The game will start with instructions and determine if a save file exists
    The user will be prompted to either use the save data or start a new game
    """
    #initial introduction to PeasCant Quest
    tprint("Let's Quest", font="epic",chr_ignore=True)
    print(stringResponses["complexInstructions"])

    start_game = input("Are you ready to begin the quest?? y/n: ")

    if start_game.lower() == "y":

        try:
            with open('PythonPeasantQuest/peasant_data.pkl', 'rb') as peasant_data:
                peasant_new = pickle.load(peasant_data)
            if peasant_new: 
                save_game = input("It looks like there is a saved game, would you like to load that game? y/n: ")
                if save_game.lower() == "y":
                    dashing.inventory = peasant_new.inventory
                    dashing.dress = peasant_new.dress
                    dashing.fire = peasant_new.fire
                    dashing.stink = peasant_new.stink 
                    gameStart(peasant_new.storyframe,[15,5])
                else: 
                    os.system("clear")
                    load_animation("Booting sad peasantry....")

                    tprint("HOUSE", font="fire_font-s", chr_ignore=True)
                    aprint("at what cost")

                    print(stringResponses["introText"])

                    begin = input("\nPress ENTER to BEGIN\n")
                    if begin.lower() != "q":

                        os.system("clear")
                        load_animation("Awaaaay we goooo....")
                        gameStart('B3',[15,5])
        except: 
            pass

        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print(stringResponses["introText"])

        mv = input("\nPress ENTER to BEGIN\n")
        if(mv.lower() != "q"):
            os.system("clear")
            load_animation("Awaaaay we goooo....")
            gameStart('B3',[15,5])       
    else: 
        print("Come back again... if you are peasanty enough!!")

if __name__ == "__main__":
    main()

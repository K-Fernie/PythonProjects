import os
import pickle
from travelAnimation import load_animation
from gameStart import gameStart
from globalData import stringResponses, dashing
from art import tprint, aprint
from PeasantClasses import Peasant


def main():

    #initial introduction to PeasCant Quest
    tprint("Let's Quest", font="epic",chr_ignore=True)
    print(stringResponses["complexInstructions"])

    startGame = input("Are you ready to begin the quest?? y/n: ")

    if startGame.lower() == "y":

        try:
            with open('PythonPeasantQuest/peasant_data.pkl', 'rb') as peasantData:
                peasantNew = pickle.load(peasantData)
            if peasantNew: 
                saveGame = input("It looks like there is a saved game, would you like to load that game? y/n: ")
                if saveGame.lower() == "y":
                    dashing.inventory = peasantNew.inventory
                    dashing.dress = peasantNew.dress
                    dashing.fire = peasantNew.fire
                    dashing.stink = peasantNew.stink 
                    gameStart(peasantNew.storyframe,[15,5])
                else: 
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
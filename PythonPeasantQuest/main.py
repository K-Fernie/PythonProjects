from art import *
import os
from travelAnimation import load_animation
from gameStart import gameStart
from globalInfo import instructions, introText


def main():

    #initial introduction to PeasCant Quest
    tprint("PeasCant Quest", font="epic",chr_ignore=True)
    print(instructions["complexInstructions"])

    startGame = input("Are you ready to begin the quest?? y/n: ")

    if startGame.lower() == "y":
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print(introText)

        mv = input("\nPress ENTER to BEGIN\n")
        if(mv.lower() != "q"):
            os.system("clear")
            load_animation("Awaaaay we goooo....")
            #TODO - uncomment this  code when you are ready to test, right now building out the bones
            gameStart('B3')
            
    else: 
        print("Come back again... if you are peasanty enough!!")

if __name__ == "__main__":
    main()
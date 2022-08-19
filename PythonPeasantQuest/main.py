"""
Author : Kaitlyn Fernelius
Main function to be run at runtime, this is the only entry point to the game
"""
import os
import pickle
from art import tprint, aprint
from helper_functions import load_animation
from game_start import game_start
from global_data import string_response, dashing

def main():
    """
    The game will start with instructions and determine if a save file exists
    The user will be prompted to either use the save data or start a new game
    """
    #initial introduction to PeasCant Quest
    tprint("Let's Quest", font="epic",chr_ignore=True)
    print(string_response("complexInstructions"))
    start_game = input("Are you ready to begin the quest?? y/n: ")
    if start_game.lower() == "y":
        #Try Catch to determine if there is peasant data saved in the file
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
                    game_start(peasant_new.storyframe,[15,5])
                else:
                    os.system("clear")
                    load_animation("Booting sad peasantry....")
                    tprint("HOUSE", font="fire_font-s", chr_ignore=True)
                    aprint("at what cost")
                    print(string_response("introText"))
                    begin = input("\nPress ENTER to BEGIN\n")
                    if begin.lower() != "q":
                        os.system("clear")
                        load_animation("Awaaaay we goooo....")
                        game_start('B3',[15,5])
        #exception for an empty file
        except EOFError:
            pass
        #exception to handle corrupted data in the file
        except pickle.UnpicklingError:
            os.remove('PythonPeasantQuest/peasant_data.pkl')
        #exception to handle when the file has been deleted due to corruption
        except FileNotFoundError:
            pass
        #If no file exists continue with booting the game for the first time UX
        os.system("clear")
        load_animation("Booting sad peasantry....")

        tprint("HOUSE", font="fire_font-s", chr_ignore=True)
        aprint("at what cost")

        print(string_response("introText"))

        begin = input("\nPress ENTER to BEGIN\n")
        if begin.lower() != "q":
            os.system("clear")
            load_animation("Awaaaay we goooo....")
            game_start('B3',[15,5])
    else:
        print("Come back again... if you are peasanty enough!!")

if __name__ == "__main__":
    main()

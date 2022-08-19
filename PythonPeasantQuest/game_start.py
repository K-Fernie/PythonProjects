"""
game_start is where the game is initialized.
The Game screen and the death screen are shown as needed during the game loop
"""
import curses
from curses.textpad import Textbox
from global_data import string_responses,dashing, dash_objectives, dash_objectives_copy
from helper_functions import text_interact, enter_is_terminate



def dead_guy(screen):
    """
    The user is sent to the death screen for three different death events:
    1. Killed by the Kerrek
    2. Killed by the Johnka
    3. Facing Trogdor too soon
    """
    #initiating the screen
    curses.initscr()
    win = curses.newwin(30, 60, 1, 1)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    sub = win.subwin(10, 60, 21, 1)
    sub.border()
    sub_2 = sub.subwin(8, 58, 22, 2)
    txt_box = curses.textpad.Textbox(sub_2)
    win.refresh()

    for i in range(1,20):
        win.addstr(i,1,dash_objectives.objective_dict[screen]["map"][i])

    #Setting boolean to break the game loop
    close_screen = False

    while not close_screen:
        #Clearing and refreshing to capture the screen information for the text screen
        sub_2.clear()
        sub_2.refresh()

        win.addstr(20, 2, f' {screen} ')

        event = win.getch()

        if event == curses.KEY_END:
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
            sub_2.addstr(string_responses["playAgain"])
            txt_box.edit(enter_is_terminate)
            contents = txt_box.gather().split("??:", 1)[1]
            cont_res = "".join(contents).strip().lower()
            if cont_res == "y":
                dashing.inventory = []
                dashing.dress = False
                dashing.fire = False
                dashing.stink = False
                dash_objectives.objective_dict = dash_objectives_copy
                game_start("B3", [15,5])
            elif cont_res == "n":
                close_screen = True
            else:
                sub_2.addstr("I didn't get that, would you like to play again ??:")

    curses.endwin()

"""
Initializing game play for Peasants Quest
The goal is to get all the items needed to:
1. Dress like a peasant
2. Stink like a peasant
3. Be on fire like a peasant
"""
def game_start(screen,heroloc):
    """Setting the screen for the game play"""
    dashing.storyframe = screen
    #initiating the screen
    curses.initscr()
    win = curses.newwin(30, 60, 1, 1)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    sub = win.subwin(10, 60, 21, 1)
    sub.border()
    sub_2 = sub.subwin(8, 58, 22, 2)
    txt_box = curses.textpad.Textbox(sub_2)
    win.refresh()

    #Initiating list to track the current map's obstacles
    obs_list = []
    #create view and create obstacle list
    for i in range(1,20):
        win.addstr(i,1,dash_objectives.objective_dict[screen]["map"][i])
        for j in range(len(dash_objectives.objective_dict[screen]["map"][i])):
            if dash_objectives.objective_dict[screen]["map"][i][j] != " ":
                obs_list.append([i,j+1])


    hero_img = '\u265E'
    hero = list(heroloc)
    win.addch(hero[0], hero[1], hero_img)

    #Extra data for if the screen is "C4" with the Kerrek
    if screen == "C4" or screen == "B1" and "belt" not in dashing.inventory:
        kerrekloc = [2,45]
        kerrek = "\\(⊙ \ _ /◎)/"

        win.refresh()
        pass


    #Setting booleans for screen control  
    down = True
    left = True
    close_screen = False
    #initiating game loop
    while not close_screen:
        #Clearing and refreshing to capture the screen information for the text screen
        sub_2.clear()
        sub_2.refresh()

        win.addstr(20, 2, f' {screen} ')

        #Determining Exit Locations and adding exits accordingly
        north_exit,west_exit,south_exit,east_exit = False, False, False, False
        if "north" in dash_objectives.objective_dict[screen]["exit"]:
            win.addstr(0, 25, ' Exit North ')
            north_exit = True

        if "east" in dash_objectives.objective_dict[screen]["exit"]:
            win.addch(7, 59, ' ')
            win.addch(8, 59, 'E')
            win.addch(9, 59, 'a')
            win.addch(10, 59, 's')
            win.addch(11, 59, 't')
            win.addch(12, 59, ' ')
            east_exit = True

        if "west" in dash_objectives.objective_dict[screen]["exit"]:
            win.addch(7, 0, ' ')
            win.addch(8, 0, 'W')
            win.addch(9,0, 'e')
            win.addch(10, 0, 's')
            win.addch(11,0, 't')
            win.addch(12, 0, ' ')
            west_exit = True

        if "south" in dash_objectives.objective_dict[screen]["exit"]:
            win.addstr(20, 25, ' Exit South ')
            south_exit = True

        event = win.getch()

        y = hero[0]
        x = hero[1]
        if screen == "Dead_Screen":
            dead_guy(sub_2, txt_box)
        if event == curses.KEY_END:
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
            text_interact(sub_2, txt_box, string_responses["screenInitText"], screen)
        if event == curses.KEY_DOWN:
            y += 1
            try:

                if y == 20:
                    curses.endwin()
                    game_start(dash_objectives.objective_dict[screen]["exit"].get("south"),[1,30])
                    break
                elif y == 19 and (x >= 25 and x < 35) and south_exit:
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], hero_img)
                elif y == 19 or [y,x] in obs_list:
                    pass
                else:
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], hero_img)
            except:
                pass
        #Ability to move the character
        if event == curses.KEY_UP:
            y -= 1
            try:
                #This is the North Exit
                if y==0:
                    curses.endwin()
                    game_start(dash_objectives.objective_dict[screen]["exit"].get("north"),[19,30])
                    break
                if y == 1 and (x >= 25 and x < 35) and north_exit:
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], hero_img)
                elif y == 1 or [y,x] in obs_list:
                    pass
                else:
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], hero_img)
            except:
                pass

        if event == curses.KEY_LEFT:
            x -= 1
            try:
                if x == 0:
                    curses.endwin()
                    game_start(dash_objectives.objective_dict[screen]["exit"].get("west"),[10,58])
                    break
                elif x == 1 and (y >= 8 and y < 12) and west_exit:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], hero_img)
                elif x == 1 or [y,x] in obs_list:
                    pass
                else:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], hero_img)
            except:
                pass

        if event == curses.KEY_RIGHT:
            x += 1
            try:
                if x == 59:
                    curses.endwin()
                    game_start(dash_objectives.objective_dict[screen]["exit"].get("east"),[10,1])
                    break
                elif x == 58 and (y >= 8 and y < 12) and east_exit:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], hero_img)
                elif x == 58 or [y,x] in obs_list:
                    pass
                else:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], hero_img)
            except:
                pass


    #KERREK SCREEN INFORMATION#
        if (screen == "C4" or screen == "B1") and "belt" not in dashing.inventory:

            win.timeout(200)
            win.addstr(kerrekloc[0], kerrekloc[1], kerrek)
            y_1=kerrekloc[0]
            x_1=kerrekloc[1]

            if y_1 == 19:
                down = False

            if y_1 == 1:
                down=True

            if x_1 == 1:
                left = False

            if x_1 == 59:
                left = True

            if (y_1 != 19 and down) and (x_1 != 1 and left):
                y_1+=1
                x_1-=2

            elif (y_1 != 1 and not down):
                y_1-=1
                x_1+=2

            win.addstr(kerrekloc[0], kerrekloc[1], "            ")
            kerrekloc[0] = y_1
            kerrekloc[1] = x_1
            win.addstr(kerrekloc[0], kerrekloc[1], kerrek)

            #Kerrek's Kill zone
            kill_zone = [
            [y_1,x_1-1],
            [y_1,x_1],
            [y_1,x_1+1],
            [y_1,x_1+2],
            [y_1,x_1+3],
            [y_1,x_1+4],
            [y_1,x_1+5],
            [y_1,x_1+6],
            [y_1,x_1+7],
            [y_1,x_1+8],
            [y_1,x_1+9],
            [y_1,x_1+10],
            [y_1,x_1+10]
            ]
            #Death Conditions

            if hero in kill_zone:
                close_screen = True
        if "sword" in dashing.inventory:
            dash_objectives.objective_dict["E2"]["exit"]["east"] = "Trog_lair"

        if "trogdor" in dashing.inventory:
            close_screen = True

    curses.endwin()
    if close_screen is True:
        dead_guy("Dead_Screen")

#Starting for testing purposes, not to be used during game
#dead_guy("Dead_Screen")
#game_start("B3",[15,5])

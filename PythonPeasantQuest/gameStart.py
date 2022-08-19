import curses
from re import sub
from globalInfo import stringResponses, getMap, dashObjectives, dashObjectivesCopy, dashing
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import contains, truediv
from travelAnimation import load_animation
from Peasant import Peasant
from PIL import Image
from helperFunctions import textInteract, enter_is_terminate   
import json
from Objectives import Objectives

"""
The user is sent to the death screen for three different death events:
1. Killed by the Kerrek
2. Killed by the Johnka
3. Facing Trogdor too soon
"""

def deadGuy(screen):
    
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
    sub2 = sub.subwin(8, 58, 22, 2)
    tb = curses.textpad.Textbox(sub2)
    win.refresh()
    
    for i in range(1,20):
        win.addstr(i,1,dashObjectives.objectiveDict[screen]["map"][i])

    close_screen = False

    while not close_screen:
        #Clearing and refreshing to capture the screen information for the text screen
        sub2.clear()
        sub2.refresh()
        
        win.addstr(20, 2, f' {screen} ')
        
        event = win.getch()

        if event == curses.KEY_END: 
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
                sub2.addstr(stringResponses["playAgain"])
                tb.edit(enter_is_terminate)
                contents = tb.gather().split("??:", 1)[1]
                contRes = "".join(contents).strip().lower()
                if contRes == "y":
                    dashing.inventory = []
                    dashing.dress = False
                    dashing.fire = False
                    dashing.stink = False
                    dashObjectives.objectiveDict = dashObjectivesCopy
                    gameStart("B3", [15,5])
                elif contRes == "n":
                    close_screen = True
                else:
                    sub2.addstr("I didn't get that, would you like to play again ??:")

    curses.endwin()
       

def gameStart(screen,heroloc):
    """Setting the screen for the game play"""
    

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
    sub2 = sub.subwin(8, 58, 22, 2)
    tb = curses.textpad.Textbox(sub2)
    win.refresh()
    
    #Initiating list to track the current map's obstacles
    obsList = []
    #create view and create obstacle list
    for i in range(1,20):
        win.addstr(i,1,dashObjectives.objectiveDict[screen]["map"][i])
        for j in range(len(dashObjectives.objectiveDict[screen]["map"][i])): 
            if dashObjectives.objectiveDict[screen]["map"][i][j] != " ":
                obsList.append([i,j+1])
        

    heroImg = '\u265E'
    hero = list(heroloc)
    win.addch(hero[0], hero[1], heroImg)

    #Extra data for if the screen is "C4" with the Kerrek
    if screen == "C4" or screen == "B1" and "belt" not in dashing.inventory:
        kerrekloc = [2,45]
        kerrek = "\(⊙ \ _ /◎)/"
        
        win.refresh()
        pass
 
    
    #Setting booleans for screen control
    
    down = True
    left = True
    close_screen = False
    #initiating game loop
    while not close_screen:
        #Clearing and refreshing to capture the screen information for the text screen
        sub2.clear()
        sub2.refresh()
        
        win.addstr(20, 2, f' {screen} ')

        #Determining Exit Locations and adding exits accordingly
        northExit,westExit,southExit,eastExit = False, False, False, False
        if "north" in dashObjectives.objectiveDict[screen]["exit"]:
            win.addstr(0, 25, ' Exit North ') #10 characters starting at 25 if x is between 25 - 30
            northExit = True

        if "east" in dashObjectives.objectiveDict[screen]["exit"]: 
            win.addch(7, 59, ' ')   
            win.addch(8, 59, 'E')
            win.addch(9, 59, 'a')
            win.addch(10, 59, 's')
            win.addch(11, 59, 't')
            win.addch(12, 59, ' ')
            eastExit = True

        if "west" in dashObjectives.objectiveDict[screen]["exit"]:
            win.addch(7, 0, ' ')   
            win.addch(8, 0, 'W')
            win.addch(9,0, 'e')
            win.addch(10, 0, 's')
            win.addch(11,0, 't')
            win.addch(12, 0, ' ')
            westExit = True

        if "south" in dashObjectives.objectiveDict[screen]["exit"]:
            win.addstr(20, 25, ' Exit South ')
            southExit = True 
        
        event = win.getch()

        y = hero[0]
        x = hero[1]
        if screen == "Dead_Screen":     
            deadGuy(sub2, tb) 
        if event == curses.KEY_END: 
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
            textInteract(sub2, tb, stringResponses["screenInitText"], screen)
        if event == curses.KEY_DOWN:
            y += 1
            try:
                
                if y == 20: 
                    curses.endwin()
                    gameStart(dashObjectives.objectiveDict[screen]["exit"].get("south"),[1,30])
                    break
                elif y == 19 and (x >= 25 and x < 35) and southExit: 
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], heroImg)
                elif y == 19 or [y,x] in obsList: 
                    pass
                else:
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], heroImg)
            except:
                pass
        #Ability to move the character 
        if event == curses.KEY_UP:
            y -= 1
            try:
                #This is the North Exit
                if y==0: 
                    curses.endwin()
                    gameStart(dashObjectives.objectiveDict[screen]["exit"].get("north"),[19,30])
                    break
                if y == 1 and (x >= 25 and x < 35) and northExit: 
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], heroImg)
                elif y == 1 or [y,x] in obsList: 
                    pass
                else: 
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], heroImg)
            except:
                pass

        if event == curses.KEY_LEFT:
            x -= 1
            try:
                if x == 0: 
                    curses.endwin()
                    gameStart(dashObjectives.objectiveDict[screen]["exit"].get("west"),[10,58])
                    break
                elif x == 1 and (y >= 8 and y < 12) and westExit:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
                elif x == 1 or [y,x] in obsList:
                    pass
                else: 
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
            except:
                pass

        if event == curses.KEY_RIGHT: 
            x += 1
            try:
                if x == 59: 
                    curses.endwin()
                    gameStart(dashObjectives.objectiveDict[screen]["exit"].get("east"),[10,1])
                    break
                elif x == 58 and (y >= 8 and y < 12) and eastExit:
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
                elif x == 58 or [y,x] in obsList: 
                    pass
                else: 
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
            except:
                pass


    #KERREK SCREEN INFORMATION#
        if (screen == "C4" or screen == "B1") and "belt" not in dashing.inventory:
            
            win.timeout(200)
            win.addstr(kerrekloc[0], kerrekloc[1], kerrek)
            y1=kerrekloc[0]
            x1=kerrekloc[1]

            if y1 == 19: 
                down = False
            
            if y1 == 1: 
                down=True
            
            if x1 == 1: 
                left = False
            
            if x1 == 59: 
                left = True

            if (y1 != 19 and down) and (x1 != 1 and left):
                y1+=1
                x1-=2

            elif (y1 != 1 and not down):
                y1-=1
                x1+=2
            
            win.addstr(kerrekloc[0], kerrekloc[1], "            ")
            kerrekloc[0] = y1
            kerrekloc[1] = x1
            win.addstr(kerrekloc[0], kerrekloc[1], kerrek)
            
            #Kerrek's Kill zone
            killZone = [
            [y1,x1-1],
            [y1,x1],
            [y1,x1+1],
            [y1,x1+2],
            [y1,x1+3],
            [y1,x1+4],
            [y1,x1+5],
            [y1,x1+6],
            [y1,x1+7],
            [y1,x1+8],
            [y1,x1+9],
            [y1,x1+10],
            [y1,x1+10]
            ]
            #Death Conditions
          
            if hero in killZone:
                close_screen = True 
                
    curses.endwin()
    if close_screen == True:
        deadGuy("Dead_Screen")            
#TODO - Finish writing the requirements for the JSON file 
#TODO - Write out fight simulation with Trogdor
#TODO - Add comments
#TODO- Move helper functions to a separate file
#TODO- If user types "Save" save the current status of dashing in a local text file
#TODO- 
# initiating separate from main for testing purposes only

#deadGuy("Dead_Screen") 
gameStart("B3",[15,5]) 

            


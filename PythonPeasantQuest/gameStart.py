import curses
from globalInfo import getMap, mapObjectives, instructions, mapResponse, burntHomeLook, dashing, jerkResponse, burnenatedPaper, gotIt, dontGotIt, objCompleteLook, screenInitTxt
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import truediv
from turtle import st
from travelAnimation import load_animation
from PIL import Image



def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

#TODO - test this function and make sure it works as intended 
def subRefresh(subwin, txtwin, witty_response, location):
    subwin.clear()
    subwin.refresh()
    textInteract(subwin, txtwin, witty_response, location)


#TODO-This needs heavy testing to make sure that the validation for the map is working
def textInteract(subwin, txtwin, witty_response, location):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather().split("??:", 1)[1]
    s = ""
    contRes = s.join(contents).strip().lower() 
    dashingObj = dashing.inventory["map"]

    if "map" in contRes:
        if not dashingObj:
            subRefresh(subwin,txtwin,dontGotIt)
        else:
            with Image.open(getMap(location)) as img: 
                img.show()
            subRefresh(subwin,txtwin,mapResponse,location)
            
    elif contRes == "look":
        if dashingObj:
            subRefresh(subwin,txtwin,objCompleteLook, location)
        else: 
            subRefresh(subwin,txtwin,burntHomeLook, location)

    elif contRes == "help": 
        subRefresh(subwin,txtwin,instructions["simpleInstructions"], location)

    elif contRes == "get paper":
        if not dashingObj:
            dashing.inventory["map"] = True
            subRefresh(subwin,txtwin,burnenatedPaper, location)
        else: 
            subRefresh(subwin, txtwin, gotIt, location)

    elif contRes == "done":
        pass

    else: 
        subRefresh(subwin,txtwin,jerkResponse, location)

def gameStart(screen):
    #list that tracks obstacles 
    obsList = []

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
    
    #create view and create obstacle list
    for i in range(1,20):
        win.addstr(i,1,mapObjectives[screen]["map"][i])
        for j in range(len(mapObjectives[screen]["map"][i])): 
            if mapObjectives[screen]["map"][i][j] is not " ":
                obsList.append([i,j+1])
        

    heroImg = '\u265E'
    hero = [10,20]
    win.addch(hero[0], hero[1], heroImg)

    close_screen = False
    
    #initiating game loop
    while not close_screen:

        northExit = False

        sub2.clear()
        sub2.refresh()
        win.addstr(20, 2, f' {screen} ')
        
        if "north" in mapObjectives[screen]["exit"]:
            win.addstr(0, 25, ' Exit North ') #10 characters starting at 25 if x is between 25 - 30
            northExit = True

        if "east" in mapObjectives[screen]["exit"]: 
            win.addch(7, 59, ' ')   
            win.addch(8, 59, 'E')
            win.addch(9, 59, 'a')
            win.addch(10, 59, 's')
            win.addch(11, 59, 't')
            win.addch(12, 59, ' ')
            eastExit = True

        if "west" in mapObjectives[screen]["exit"]:
            win.addch(7, 0, ' ')   
            win.addch(8, 0, 'W')
            win.addch(9,0, 'e')
            win.addch(10, 0, 's')
            win.addch(11,0, 't')
            win.addch(12, 0, ' ')
            westExit = True

        if "south" in mapObjectives[screen]["exit"]:
            win.addstr(20, 25, ' Exit South ')
            southExit = True 
            
        event = win.getch()

        y = hero[0]
        x = hero[1]

        if event == curses.KEY_END: 
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
            textInteract(sub2, tb, screenInitTxt, screen)
        if event == curses.KEY_DOWN:
            y += 1
            try:
                
                if y == 20: 
                    curses.endwin()
                    gameStart(mapObjectives[screen]["exit"].get("south"))
                    break
                elif y == 19 and (x >= 25 and x < 35): 
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
                    gameStart(mapObjectives[screen]["exit"].get("north"))
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
                    gameStart(mapObjectives[screen]["exit"].get("west"))
                    break
                elif x == 1 and (y >= 8 and y < 12):
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
                elif [y,x] in obsList:
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
                    gameStart(mapObjectives[screen]["exit"].get("east"))
                    break
                elif x == 58 and (y >= 8 and y < 12):
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

#Check that there isn't a character at a certain position, if there is then you can move the character, if not no go

# initiating separate from main for testing purposes only
gameStart("B3") 

            


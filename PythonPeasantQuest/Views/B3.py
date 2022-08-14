import curses
from Utilities.globalInfo import simplelInstructions, mapPath, mapResponse, burntHomeLook, dashing, jerkResponse, burnenatedPaper, gotIt, dontGotIt, objCompleteLook, screenInitTxt
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import truediv
from turtle import st
from Utilities.travelAnimation import load_animation
from PIL import Image



def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

#TODO - test this function and make sure it works as intended 
def subRefresh(subwin, txtwin, witty_response):
    subwin.clear()
    subwin.refresh()
    textInteract(subwin, txtwin, witty_response)


#TODO-This needs heavy testing to make sure that the validation for the map is working
def textInteract(subwin, txtwin, witty_response):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather().split("??:", 1)[1]
    s = ""
    contRes = s.join(contents).strip().lower() 
    dashingObj = dashing.inventory["map"]

    if contRes == "map":
        if not dashingObj:
            subRefresh(subwin,txtwin,dontGotIt)
        else:
            subRefresh(subwin,txtwin,mapResponse)
            #TODO - add coordinates to the mapResponse
            with Image.open(mapPath) as img: 
                img.show()

    elif contRes == "look":
        if dashingObj:
            subRefresh(subwin,txtwin,objCompleteLook)
        else: 
            subRefresh(subwin,txtwin,burntHomeLook)

    elif contRes == "help": 
        subRefresh(subwin,txtwin,simplelInstructions)

    elif contRes == "get paper":
        if not dashingObj:
            dashing.inventory["map"] = True
            subRefresh(subwin,txtwin,burnenatedPaper)
        else: 
            subRefresh(subwin, txtwin, gotIt)

    elif contRes == "done":
        pass

    else: 
        subRefresh(subwin,txtwin,jerkResponse)

def peasantHome():

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
    

    heroImg = '\u265E'
    hero = [10,20]
    win.addch(hero[0], hero[1], heroImg)

    win.addch(item1[0], item1[1], "*")
    item1 = [2, 15]

    key = None
    close_screen = False
    #game logic
    while not close_screen:
        sub2.clear()
        sub2.refresh()

        win.addstr(20, 2, ' HOME SCENE ')
        win.addstr(0, 25, 'Exit North') #10 characters starting at 25 if x is between 25 - 30
        win.addch(8, 59, 'E')
        win.addch(9, 59, 'a')
        win.addch(10, 59, 's')
        win.addch(11, 59, 't')
        
        event = win.getch()

        y = hero[0]
        x = hero[1]

        if event == curses.KEY_END: 
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME:
            textInteract(sub2, tb, screenInitTxt)
        if event == curses.KEY_DOWN:
            y += 1
            try:
                if y == 19:
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
                    load_animation("Let's gooooo North")
                    #northHome()
                    break
                if y == 1 and (x >= 25 and x < 35): 
                    #TODO - call new window (Different Scene)
                    win.addch(hero[0], hero[1], " ")
                    hero[0] = y
                    win.addch(hero[0], hero[1], heroImg)
                elif y == 1: 
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
                    load_animation("Let's Go East")
                    break
                elif x == 58 and (y >= 8 and y < 12):
                    #TODO - kill current window and add the start to a new scene
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
                elif x == 58: 
                    pass
                else: 
                    win.addch(hero[0], hero[1], " ")
                    hero[1] = x
                    win.addch(hero[0], hero[1], heroImg)
            except:
                pass

# initiating separate from main for testing purposes only
#peasantHome()  

            


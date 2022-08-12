import curses
from globalInfo import simplelInstructions, mapPath
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import truediv
from turtle import st
from A3 import northHome
from travelAnimation import load_animation
from PIL import Image



def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x
    

def textInteract(subwin, txtwin, witty_response):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather().split("??:", 1)[1]
    s = ""
    contRes = s.join(contents).strip().lower() 

    if contRes == "map":
        #only show if the peasant has burninated paper (if not say "You're inventory doesn't have that biz") 
        with Image.open(mapPath) as img: 
            img.show()
        witty_response = "Now that you know where you are....\nWhat do you do ??:"
        subwin.clear()
        subwin.refresh()
        textInteract(subwin, txtwin, witty_response)
    elif contRes == "look":
        witty_response = "You see a poor burnt cottage\nNear the cottage lies a burnt paper\nWhat do you do ??: "
        subwin.clear()
        subwin.refresh()
        textInteract(subwin, txtwin, witty_response)
    elif contRes == "help": 
        witty_response = simplelInstructions
        subwin.clear()
        subwin.refresh()
        textInteract(subwin, txtwin, witty_response)
    elif contRes == "get paper":
        witty_response = "You pick up the burnenated paper\nITS A MAP!!\n"\
            "Now you won't be poor AND lost\nTo access the fragile map, type 'map'\n"\
            "What do you do ??:"
        subwin.clear()
        subwin.refresh()
        textInteract(subwin, txtwin, witty_response)
    elif contRes == "done":
        pass
    else: 
        witty_response = "You would like to get that wouldn't you ??: "
        subwin.clear()
        subwin.refresh()
        textInteract(subwin, txtwin, witty_response)

def peasantHome():
    #Basic logic to create a screen
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
    item1 = [2, 15]
    win.addch(hero[0], hero[1], heroImg)
    win.addch(item1[0], item1[1], "*")
    key = None;

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
            witty_response = "Type 'done' to exit text mode\nWhat do you want poor peasant??: " 
            textInteract(sub2, tb, witty_response)
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
                    northHome()
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
# peasantHome()  

            


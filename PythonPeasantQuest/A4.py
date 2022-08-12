import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import truediv
from turtle import st
from A3 import northHome
from travelAnimation import load_animation
import os
from PIL import Image
import time


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

        win.addstr(20, 2, 'HOME SCENE')
        win.addstr(0, 25, 'Exit North') #10 characters starting at 25 if x is between 25 - 30
        win.addch(8, 59, 'E')
        win.addch(9, 59, 'a')
        win.addch(10, 59, 's')
        win.addch(11, 59, 't')
        
        event = win.getch()

        y = hero[0]
        x = hero[1]

        witty_response = "What do you want poor boy??: "
        if event == curses.KEY_END: 
            curses.beep()
            close_screen = True
        if event == curses.KEY_HOME: 
            sub2.addstr(witty_response)
            tb.edit()
            contents = tb.gather().split("??:", 1)[1]
            s = ""
            contRes = s.join(contents).strip().lower() 
            if contRes == "map": 
                with Image.open('PythonPeasantQuest\images\peasantmap.png') as img: 
                    img.show()
            else: 
                witty_response = "You would like to get that wouldn't you ??:"
                event = curses.KEY_HOME
            #TODO - Determine certain actions based on the user input
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

peasantHome()
    
    
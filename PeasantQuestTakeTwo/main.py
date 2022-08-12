import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

#Instructions : 
# q will end the program
# 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    WHITE_ON_WHITE = curses.color_pair(3)
    
    #Setting Up the screen
    stdscr.nodelay(True)
    win = curses.newwin(3,18,2,2)
    box = Textbox(win)
    

    x, y = 10, 10
    key = None
    hero = "┌( ಠ_ಠ)┘"

   
        
    try: 
        key = stdscr.getkey()
    except: 
        key = None 

    if key == "KEY_LEFT": 
        x -= 1
    elif key == "KEY_RIGHT": 
        x += 1
    elif key == "KEY_UP": 
        y -= 1
    elif key == "KEY_DOWN": 
        y += 1

        

    stdscr.clear()
    stdscr.border()
    win.addstr(1, 1, "Hello")
        
        # stdscr.addstr(0, string_x//50, "hello world")
    stdscr.addstr(y, x, hero)
    stdscr.refresh()
    win.refresh()

#wrapper initializes the screen for you
wrapper(main)
import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_WHITE = curses.color_pair(3)

    pad = curses.newpad(100, 100)
    pad.border()
    stdscr.refresh()

    for i in range(100): 
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLACK)

    #(curses.LINES -1, curses.COLS -1)
    #gets user input 
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0,0,5,5,15,25)
        time.sleep(.2)

    stdscr.getch()

#wrapper initializes the screen for you
wrapper(main)
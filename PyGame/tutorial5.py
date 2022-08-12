import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    ORANGE_AND_WHITE = curses.color_pair(3)
    curses.echo()

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)
    #use CTRL + G to get out of the text box
   
    stdscr.attron(BLUE_AND_YELLOW)
    stdscr.border()
    stdscr.attroff(BLUE_AND_YELLOW)

    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.attroff(GREEN_AND_BLACK)

    stdscr.addstr(5,30, "Hello world!")
    
    stdscr.move(10,20)

    stdscr.refresh()

    while True: 
        key = stdscr.getkey()
        if key == "q": 
            break
    
    stdscr.getch()
    

    

#wrapper initializes the screen for you
wrapper(main)
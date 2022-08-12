import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 10, "Hello World")
    stdscr.addstr(13,15, "This is me")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
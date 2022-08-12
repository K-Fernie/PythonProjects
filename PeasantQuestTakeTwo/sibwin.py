import curses
from curses.textpad import Textbox, rectangle

def setup_input():
    curses.initscr()
    inp = curses.newwin(8,55, 0,0)
    inp.border()
    inp.addstr(1,1, "Please enter your username:")
    sub = inp.subwin(3, 41, 2, 1)
    sub.border()
    sub2 = sub.subwin(1, 40, 3, 2)
    tb = curses.textpad.Textbox(sub2)
    inp.refresh()
    tb.edit()

setup_input()
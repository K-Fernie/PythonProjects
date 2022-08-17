import curses
from re import sub
from globalInfo import getMap, mapObjectives, instructions, mapResponse, burntHomeLook, dashing, jerkResponse, burnenatedPaper, gotIt, dontGotIt, objCompleteLook, screenInitTxt
from curses import wrapper
from curses.textpad import Textbox, rectangle
from operator import contains, truediv
from turtle import st
from travelAnimation import load_animation
from PIL import Image

def enter_is_terminate(x):
    if x == 10:
        x = 7
    return x

def lookItem(subwin,txtwin, location):
    itemCount = 0
    itemKey = mapObjectives[location]["items"]
    printstring = ""
    if itemKey:
        for item in itemKey:
            description = itemKey[item]["description"]
            if itemCount == 0:
                printstring+=f"You look and see a {description}"
                itemCount += 1
            else: 
                printstring+=f" and a {description}\n"
        printstring += "What do you do ??:"
        subRefresh(subwin,txtwin,printstring,location)
    else: 
        subRefresh(subwin,txtwin,objCompleteLook,location)

def getItem(subwin,txtwin,location,item):
    itemObj = mapObjectives[location]["items"]

    if item in itemObj and item not in dashing.inventory:
        prereqs = itemObj[item]["prereqs"]
        if (prereqs != "None" and prereqs in dashing.inventory) or (prereqs == "None"):
            response = itemObj[item]["get"]
            del itemObj[item]
            dashing.inventory.append(item)
        else: 
            response = itemObj[item]["noprereqs"]
        subRefresh(subwin,txtwin,response,location)
    else: 
        response = "You can't get that, What do you do ??:"
        subRefresh(subwin,txtwin,response,location)

def talkNPC(subwin,txtwin,location):
    pass


def subRefresh(subwin, txtwin, witty_response, location):
    subwin.clear()
    subwin.refresh()
    textInteract(subwin, txtwin, witty_response, location)


def textInteract(subwin, txtwin, witty_response, location):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather().split("??:", 1)[1]
    s = ""
    contRes = s.join(contents).strip().lower()
    

    if contRes == "map":
        if "map" in dashing.inventory:
            with Image.open(getMap(location)) as img: 
                img.show()
            subRefresh(subwin,txtwin,mapResponse,location)
        else:
            subRefresh(subwin,txtwin,dontGotIt,location)
    elif contRes == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        subRefresh(subwin,txtwin,inv,location)

    elif "look" in contRes:
        lookItem(subwin,txtwin, location)

    elif "get" in contRes:
        getItem(subwin,txtwin,location,contRes[4:])

    elif contRes == "help": 
        subRefresh(subwin,txtwin,instructions["simpleInstructions"], location)

   

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
            if mapObjectives[screen]["map"][i][j] != " ":
                obsList.append([i,j+1])
        

    heroImg = '\u265E'
    hero = [15,5]
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


# initiating separate from main for testing purposes only
gameStart("B3") 

            


import curses
from re import sub
from globalInfo import stringResponses, getMap, mapObjectives, dashing
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
                printstring+=f"You look and see {description}"
                itemCount += 1
            else: 
                printstring+=f" and {description}\n"
        printstring += "What do you do ??:"
        subRefresh(subwin,txtwin,printstring,location)
    else: 
        subRefresh(subwin,txtwin,stringResponses["objCompleteLook"],location)

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


def subRefresh(subwin, txtwin, witty_response, location):
    subwin.clear()
    subwin.refresh()
    textInteract(subwin, txtwin, witty_response, location)


def textInteract(subwin, txtwin, witty_response, location):

    subwin.addstr(witty_response)
    txtwin.edit(enter_is_terminate)
    contents = txtwin.gather().split("??:", 1)[1]
    contRes = "".join(contents).strip().lower()
    

    if contRes == "map":
        if "map" in dashing.inventory:
            with Image.open(getMap(location)) as img: 
                img.show()
            subRefresh(subwin,txtwin,stringResponses["mapResponse"],location)
        else:
            subRefresh(subwin,txtwin,stringResponses["dontGotIt"],location)
    elif contRes == "inventory":
        inv = f"Inventory: {dashing.inventory}\nWhat do you do ??: "
        subRefresh(subwin,txtwin,inv,location)

    elif "look" in contRes:
        lookItem(subwin,txtwin, location)

    elif "get" in contRes:
        getItem(subwin,txtwin,location,contRes[4:])

    elif contRes == "help": 
        subRefresh(subwin,txtwin,stringResponses["simpleInstructions"], location)

    elif contRes == "done":
        pass
    elif contRes == "save":
        #TODO - pass a timestamp, and the peasant information to a save file
        pass
    else: 
        subRefresh(subwin,txtwin,stringResponses["jerkResponse"], location)

def gameStart(screen,heroloc):
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
    hero = heroloc
    win.addch(hero[0], hero[1], heroImg)

    close_screen = False
    
    #initiating game loop
    while not close_screen:

        northExit,westExit,southExit,eastExit = False, False, False, False

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
            textInteract(sub2, tb, stringResponses["screenInitText"], screen)
        if event == curses.KEY_DOWN:
            y += 1
            try:
                
                if y == 20: 
                    curses.endwin()
                    gameStart(mapObjectives[screen]["exit"].get("south"),[1,30])
                    break
                elif y == 19 and (x >= 25 and x < 35) and southExit: 
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
                    gameStart(mapObjectives[screen]["exit"].get("north"),[19,30])
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
                    gameStart(mapObjectives[screen]["exit"].get("west"),[10,58])
                    break
                elif x == 1 and (y >= 8 and y < 12) and westExit:
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
                    gameStart(mapObjectives[screen]["exit"].get("east"),[10,1])
                    break
                elif x == 58 and (y >= 8 and y < 12) and eastExit:
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

#TODO - Add a hero location to game start and then modify it based on where they are entering from 
#TODO - Finish writing the requirements for the JSON file 
#TODO - Write out fight simulation with Trogdor
#TODO - Figure out if global info would be better suited as a JSON file too
#TODO - Add comments
#TODO- Move helper functions to a separate file
#TODO- Figure out the Kerrek (moving item that could kill you if you are overlapped)
#TODO- If user types "Save" save the current status of dashing in a local text file
#TODO- 
# initiating separate from main for testing purposes only
#gameStart("B3",[15,5]) 

            


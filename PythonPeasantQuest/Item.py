from curses import ACS_DARROW
from mailbox import Babyl
from winreg import REG_NOTIFY_CHANGE_SECURITY


class Item: 

    def __init__(self, name, description, used):
        self.name = name
        self.descriptoin = description
        self.used = used

global map
global pebbles
global monsterMaskus
global arrow
global kerrekBelt
global trinket
global superTimeFunBow
global muddyBoy
global chickenFeed
global hayCover
global riches
global baby
global nakedManRobe
global greaseHead
global knightSword
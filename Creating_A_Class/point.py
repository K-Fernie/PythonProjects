from operator import truediv


class Point:
    
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft[0] < self.x < rectangle.upright[0] and rectangle.lowleft[1] < self.y < rectangle.upright[1]:
            return True
        else: 
            return False
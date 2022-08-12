from point import Point
from rectangle import Rectangle

def main():

    p1 = Point(1,5)
    p2 = Point(3,7)

    rect1 = Rectangle(p1, p2)

    pointx = Point(6,7)

    pointx.falls_in_rectangle(rect1)

main()
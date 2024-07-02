from graphics import Point, Line, Window
from cell import Cell

def main():
    w = Window(1600, 900)
    p1 = Point(0, 0)
    p2 = Point(100, 100)
    p3 = Point(200, 50)
    p4 = Point(200, 500)
    p5 = Point(0, 300)

    # w.drawLine(Line(p1, p2), "red")
    # w.drawLine(Line(p2, p3), "green")
    # w.drawLine(Line(p3, p4), "blue")
    # w.drawLine(Line(p4, p5), "blue")

    c = Cell(w)
    c.l()
    c.r()
    c.draw(Point(100, 100), Point(800, 800))
    c.reset()

    c.t()
    c.b()
    c.draw(Point(150, 150), Point(750, 750))

    c.l()
    c.bWall = False
    c.draw(Point(200, 200), Point(700, 700))
    c.reset()

    c.r()
    c.b()
    c.draw(Point(250, 250), Point(650, 650))


    w.waitForClose()


main()









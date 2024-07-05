from graphics import Point, Line, Window
from cell import Cell
from maze import Maze

def main():
    w = Window(1600, 900)
    # p1 = Point(0, 0)
    # p2 = Point(100, 100)
    # p3 = Point(200, 50)
    # p4 = Point(200, 500)
    # p5 = Point(0, 300)

    # w.drawLine(Line(p1, p2), "red")
    # w.drawLine(Line(p2, p3), "green")
    # w.drawLine(Line(p3, p4), "blue")
    # w.drawLine(Line(p4, p5), "blue")

    # c = Cell(w)
    # c.l()
    # c.r()
    # c.draw(Point(100, 100), Point(800, 800))
    # c.reset()
    # c.t()
    # c.b()
    # c.draw(Point(150, 150), Point(750, 750))
    # c.l()
    # c.bWall = False
    # c.draw(Point(200, 200), Point(700, 700))
    # c.reset()
    # c.r()
    # c.b()
    # c.draw(Point(250, 250), Point(650, 650))

    # c2 = Cell(w)
    # c2.all()
    # c2.draw(Point(1125, 425), Point(1175, 475))
    # c.drawMove(c2)
    # c3 = Cell(w)
    # c3.b()
    # c3.draw(Point(1125, 475), Point(1175, 525))
    # c2.drawMove(c3, True)

    m = Maze(25, 25, 34, 62, 25, 25, w)       
    #TODO: track down why maze doesn't draw... it's calling the draw command with what looks like good data
    

    w.waitForClose()


main()









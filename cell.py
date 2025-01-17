from graphics import Point, Line, BGCOLOR

class Cell:
    def __init__(self, win=None):
        self.lWall = False
        self.rWall = False
        self.tWall = False
        self.bWall = False
        self.p1 = None
        self.p2 = None
        self.win = win
        self.visited = False
    
    def __repr__(self):
        return f"Cell({self.p1}, {self.p2})"
    def __str__(self):
        return f"Cell({self.p1}, {self.p2})"

    def l(self):
        self.lWall = True
    def r(self):
        self.rWall = True
    def t(self):    
        self.tWall = True
    def b(self):    
        self.bWall = True
    def all(self):
        self.lWall = True
        self.rWall = True
        self.tWall = True
        self.bWall = True
    def none(self):
        self.lWall = False
        self.rWall = False
        self.tWall = False
        self.bWall = False
        
    def draw(self, p1, p2, color="black"):
        self.p1 = p1
        self.p2 = p2
        self.win.drawLine(Line(p1, Point(p1.x, p2.y)), color)  if self.lWall else  self.win.drawLine(Line(p1, Point(p1.x, p2.y)), BGCOLOR)
        self.win.drawLine(Line(Point(p2.x, p1.y), p2), color)  if self.rWall else  self.win.drawLine(Line(Point(p2.x, p1.y), p2), BGCOLOR)
        self.win.drawLine(Line(p1, Point(p2.x, p1.y)), color)  if self.tWall else  self.win.drawLine(Line(p1, Point(p2.x, p1.y)), BGCOLOR)
        self.win.drawLine(Line(Point(p1.x, p2.y), p2), color)  if self.bWall else  self.win.drawLine(Line(Point(p1.x, p2.y), p2), BGCOLOR)
    
    # def draw(self, x1, y1, x2, y2):
    #     self.draw(Point(x1, y1), Point(x2, y2))

    def reset(self):
        self.lWall = False
        self.rWall = False
        self.tWall = False
        self.bWall = False
        self.p1 = None
        self.p2 = None

    def drawMove(self, cell, undo=False):
        p1 = Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
        p2 = Point((cell.p1.x+cell.p2.x)/2, (cell.p1.y+cell.p2.y)/2)
        color = "green"
        if undo:
            color = "red"
        self.win.drawLine(Line(p1, p2), color)





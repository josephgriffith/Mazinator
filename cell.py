from graphics import Point, Line

class Cell:
    def __init__(self, win):
        self.lWall = False
        self.rWall = False
        self.tWall = False
        self.bWall = False
        self.p1 = None
        self.p2 = None
        self.win = win
    
        #WTF Python, no method/constructor overloading???

    def l(self):
        self.lWall = True
    def r(self):
        self.rWall = True
    def t(self):    
        self.tWall = True
    def b(self):    
        self.bWall = True
        
    def draw(self, p1, p2):
        # self.p1 = p1
        # self.p2 = p2
        if self.lWall:
            self.win.drawLine(Line(p1, Point(p1.x, p2.y)))       #(self.p1, Point(self.p1.x, self.p2.y)))  
        if self.rWall:
            self.win.drawLine(Line(Point(p2.x, p1.y), p2))       #(Point(self.p2.x, self.p1.y), self.p2))
        if self.tWall:
            self.win.drawLine(Line(p1, Point(p2.x, p1.y)))       #(self.p1, Point(self.p2.x, self.p1.y)))
        if self.bWall:
            self.win.drawLine(Line(Point(p1.x, p2.y), p2))       #(Point(self.p1.x, self.p2.y), self.p2))
        # self.reset()
    
    # def draw(self, x1, y1, x2, y2):
    #     self.draw(Point(x1, y1), Point(x2, y2))

    def reset(self):
        self.lWall = False
        self.rWall = False
        self.tWall = False
        self.bWall = False
        self.p1 = None
        self.p2 = None



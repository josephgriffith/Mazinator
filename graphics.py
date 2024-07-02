from tkinter import Tk, BOTH, Canvas
from time import sleep

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def draw(self, canvas, color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)
    
class Window:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.root = Tk()
        self.root.title("AMAZEY WINDOW")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height, bg='dark sea green')
        self.canvas.pack()
        self.running = False
    def update(self):
        self.root.update_idletasks()
        self.root.update()
    def waitForClose(self):
        self.running = True
        while self.running:
            self.update()
            sleep(0.001)
    def close(self):
        self.running = False
    def drawLine(self, line, color="black"):
        line.draw(self.canvas, color)









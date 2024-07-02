from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        print("HERE!")
        self.x = width
        self.y = height
        self.root = Tk()
        self.root.title("AMAZEY WINDOW")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        # self.canvas.pack(fill=BOTH, expand=1)
        #pack canvas with width and height
        self.canvas.pack()
        # self.canvas.create_rectangle(20, 20, 220, 220, outline="#fb0", fill="#fb0")
        self.running = False
        print("Window created!")

    def update(self):
        self.root.update_idletasks()
        self.root.update()

    def waitForClose(self):
        self.running = True
        while self.running:
            self.update()

    def close(self):
        self.running = False
        # self.root.destroy()










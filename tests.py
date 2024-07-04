import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def testMazeCreateCells1(self):
        rows = 5
        cols = 15
        w = Window(1600, 900)
        m = Maze(0, 0, rows, cols, 32, 32, w)
        self.assertEqual(len(m._cells), rows)
        self.assertEqual(len(m._cells[0]), cols)
    def testMazeCreateCells2(self):
        rows = 20
        cols = 5
        w = Window(16, 16)
        m = Maze(4, 4, rows, cols, 32, 32, w)
        self.assertEqual(len(m._cells), rows)
        self.assertEqual(len(m._cells[0]), cols)
    def testMazeCreateCells3(self):
        rows = 1
        cols = 5
        w = Window(128, 128)
        m = Maze(-16, -16, rows, cols, 32, 32, w)
        self.assertEqual(len(m._cells), rows)
        self.assertEqual(len(m._cells[0]), cols)

























# if __name__ == "__main__":
#     unittest.main()
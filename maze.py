from cell import Cell
from graphics import Point

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._createCells()
        self._breakEntranceAndExit()
    def _createCells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                c = Cell(self.win)
                c.all()
                row.append(c)
            self._cells.append(row)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._drawCell(i, j)
        # print(self._cells)
    def _drawCell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        # print(f"Drawing cell ({x1}, {y1}) to ({x2}, {y2})")
        self._animate()
    def _animate(self):
        self.win.redraw()
    def _breakEntranceAndExit(self):
        self._cells[0][0].tWall = False
        self._drawCell(0, 0)
        self._cells[self.num_rows-1][self.num_cols-1].bWall = False
        self._drawCell(self.num_rows-1, self.num_cols-1)



            
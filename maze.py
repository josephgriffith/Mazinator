from cell import Cell
from graphics import Point
from random import randrange, seed

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seednum=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            seed(seednum)
        self._cells = []
        self._createCells()
        self._breakEntranceAndExit()
        self._breakWallsRec(0, 0)
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
    def _drawCell(self, i, j, color="black"):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2), color)
        # print(f"Drawing cell ({x1}, {y1}) to ({x2}, {y2})")
        self._animate()
    def _animate(self):
        self.win.redraw()
    def _breakEntranceAndExit(self):
        self._cells[0][0].tWall = False
        self._drawCell(0, 0, "green")
        self._cells[self.num_rows-1][self.num_cols-1].bWall = False
        self._drawCell(self.num_rows-1, self.num_cols-1, "red")
    def _breakWallsRec(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = []
            self._getNeighbors(i, j, neighbors)
            if not neighbors:
                self._cells[i][j].draw(Point(self.x1+j*self.cell_size_x, self.y1+i*self.cell_size_y), 
                                       Point(self.x1+(j+1)*self.cell_size_x, self.y1+(i+1)*self.cell_size_y))
                return
            n = neighbors[randrange(len(neighbors))]
            self._tearDownThisWall(i, j, n[0], n[1])
            self._breakWallsRec(n[0], n[1])
    def _getNeighbors(self, i, j, neighbors):
        if i > 0 and not self._cells[i-1][j].visited:
            neighbors.append((i-1, j))
        if j > 0 and not self._cells[i][j-1].visited:
            neighbors.append((i, j-1))
        if i < self.num_rows-1 and not self._cells[i+1][j].visited:
            neighbors.append((i+1, j))
        if j < self.num_cols-1 and not self._cells[i][j+1].visited:
            neighbors.append((i, j+1))
    def _tearDownThisWall(self, i, j, ni, nj):
        if i < ni:
            self._cells[i][j].bWall = False
            self._cells[ni][nj].tWall = False
        elif i > ni:
            self._cells[i][j].tWall = False
            self._cells[ni][nj].bWall = False
        elif j < nj:
            self._cells[i][j].rWall = False
            self._cells[ni][nj].lWall = False
        elif j > nj:
            self._cells[i][j].lWall = False
            self._cells[ni][nj].rWall = False
        self._cells[i][j].draw(Point(self.x1+j*self.cell_size_x, self.y1+i*self.cell_size_y),
                                Point(self.x1+(j+1)*self.cell_size_x, self.y1+(i+1)*self.cell_size_y))
        self._cells[ni][nj].draw(Point(self.x1+nj*self.cell_size_x, self.y1+ni*self.cell_size_y),
                                  Point(self.x1+(nj+1)*self.cell_size_x, self.y1+(ni+1)*self.cell_size_y))
        self._animate()
    def resetVisited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
    # def solve(self):
    #     return self._solveRec(0, 0)
    # def _solveRec(self, i, j):
    #     if i == self.num_rows-1 and j == self.num_cols-1:
    #         return True
    #     neighbors = self._getNeighbors(i, j)
    #     if not neighbors:
    #         return False
    #     for n in neighbors:
            #would be nice to have helper functions letting me easily reference - 
            #   the direction of the cell and 
            #   whether or not the wall is up
            # if self._cells[n[0]][n[1]]

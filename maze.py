from cell import Cell
from graphics import Point
from random import randrange, seed
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None, breaks=.0005, seednum=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            seed(seednum)
        self.breaks = breaks
        self._cells = []
        self._createCells()
        self._breakWallsRec(0, 0)
        self._resetVisited()
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
            neighbors = self._getNeighbors(i, j)
            if not neighbors:
                self._cells[i][j].draw(self._calcPoint(i, j),
                                       self._calcPoint(i+1, j+1))
                return
            n = neighbors[randrange(len(neighbors))]
            self._tearDownThisWall(i, j, n[0], n[1])
            self._breakWallsRec(n[0], n[1])
    def _calcPoint(self, i, j):
        return Point(self.x1+j*self.cell_size_x, self.y1+i*self.cell_size_y)
    def _getNeighbors(self, i, j):
        neighbors = []
        if j > 0 and not self._cells[i][j-1].visited:
            neighbors.append((i, j-1, 'lWall'))
        if j < self.num_cols-1 and not self._cells[i][j+1].visited:
            neighbors.append((i, j+1, 'rWall'))
        if i > 0 and not self._cells[i-1][j].visited:
            neighbors.append((i-1, j, 'tWall'))
        if i < self.num_rows-1 and not self._cells[i+1][j].visited:
            neighbors.append((i+1, j, 'bWall'))
        return neighbors
    def _tearDownThisWall(self, i, j, ni, nj):      # , Mr. Gorbachev
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
        self._cells[i][j].draw(self._calcPoint(i, j),
                                self._calcPoint(i+1, j+1))
        self._cells[ni][nj].draw(self._calcPoint(ni, nj),
                                  self._calcPoint(ni+1, nj+1))
        self._animate()
    def _resetVisited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
    def solve(self):
        return self._solveRec(0, 0)
    def _solveRec(self, i, j):
        sleep(self.breaks)
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        neighbors = self._getNeighbors(i, j)
        if not neighbors:
            return False
        # for n in neighbors:                 #probably slower, but looks great if you happen to pass by the exit with a bunch more to explore
        #     wallExists = getattr(self._cells[i][j], locals()['n'][2], None)
        #     if wallExists:
        #         continue
        #     if self._isExit(n[0], n[1]):
        #         self._cells[i][j].drawMove(self._cells[n[0]][n[1]])
        #         return True
        for n in reversed(neighbors):           #HOLY SHIT so much faster... 
            wallExists = getattr(self._cells[i][j], locals()['n'][2], None)
            if wallExists:
                continue
            if self._isExit(n[0], n[1]):
                self._cells[i][j].drawMove(self._cells[n[0]][n[1]])
                return True
            # print(f"BETWEEN: {i},{j}, AND {n[0]},{n[1]} WALL IS {wallExists}")
            if not wallExists and not self._cells[n[0]][n[1]].visited:
                self._cells[i][j].drawMove(self._cells[n[0]][n[1]])
                if self._solveRec(n[0], n[1]):
                    return True
                self._cells[i][j].drawMove(self._cells[n[0]][n[1]], True)
        return False
    def _isExit(self, i, j):
        return i == self.num_rows-1 and j == self.num_cols-1
    # def _checkExit(self, i, j, n):

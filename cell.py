import import_data as dt
class Cell:
    parent = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = "Unvisited"
        self.gridheight = dt.data['height']
        self.gridwidth = dt.data['width']
        self.g = float('inf')
        self.h = float('inf')
        self.f = 0
    def coor(self):
        return [self.x, self.y]
    def __lt__(self, other):
        return self.f < other.f
    def __eq__(self, other):
        return self.coor() == other.coor()
    def is_blocked(self, g):
        if g[self.x][self.y] == -1:
            return True
        return False
    def is_valid(self):
        if self.x < 0 or self.x >= self.gridheight or self.y < 0 or self.y >= self.gridwidth:
            return False
        return True
    def check_goal(self, goal):
        if self.x == goal.x and self.y == goal.y:
            return True
        return False
    def update_neighbors(self, grid):
        self.neighbors = []
        cur = Cell(self.x, self.y)
        if cur.is_valid():
            neighbor = Cell(cur.x + 1, cur.y)
            if neighbor.is_valid() and not neighbor.is_blocked(grid): ##right
                self.neighbors.append(neighbor)
            neighbor = Cell(cur.x - 1, cur.y)
            if neighbor.is_valid() and not neighbor.is_blocked(grid): ##left
                self.neighbors.append(neighbor)
            neighbor = Cell(cur.x, cur.y + 1)
            if neighbor.is_valid() and not neighbor.is_blocked(grid):#down
                self.neighbors.append(neighbor)
            neighbor = Cell(cur.x, cur.y - 1)
            if neighbor.is_valid() and not neighbor.is_blocked(grid):#up
                self.neighbors.append(neighbor) 
    def heuristic(self, coin):
        return abs(self.x - coin.x) + abs(self.y - coin.y)
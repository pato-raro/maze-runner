import heapq
import timeit
import time
from map import Map
from bot_utils import *
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gridheight = import_dt(input_file)['height']
        self.gridwidth = import_dt(input_file)['width']
        self.g = float('inf')
        self.h = float('inf')
        self.f = 0
        self.parent = None
        self.neighbors = []
    def coor(self):
        return [self.x, self.y]
    def __lt__(self, other):
        return self.f < other.f
    def __eq__(self, other):
        return self.coor() == other.coor()
    def __hash__(self):
        return hash((self.x, self.y))
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
class AStar:
    def __init__(self, bot):
        self.bot = bot
        self.open_set = []
        self.closed_set = set()
        self.path = []
        self.start_time = time.time()
    def find_shortest_path(self, grid):
        self.open_set.append(self.bot.pos)
        self.closed_set.add(self.bot.pos)
        self.bot.pos.g = 0
        self.bot.pos.h = self.bot.pos.heuristic(self.bot.end)
        if self.bot.pos == self.bot.end:
            return self.bot.pos.coor()
        while self.open_set:
            cur_pos = heapq.heappop(self.open_set)
            cur_pos.update_neighbors(grid.map)
            if cur_pos == self.bot.end:
                while cur_pos is not None:
                    self.path.append(cur_pos.coor())
                    cur_pos = cur_pos.parent
                count = len(self.path) - 1
                ##step = self.convert_to_step(self.path[::-1])
                ##print(step)
                ##self.write_to_text(step)
                ##print(count)
                return self.path
            for i_neighbor in cur_pos.neighbors:
                temp_g = cur_pos.g + 1
                if temp_g < i_neighbor.g:
                    i_neighbor.parent = cur_pos
                    i_neighbor.g = temp_g
                    i_neighbor.h = i_neighbor.heuristic(self.bot.end)
                    i_neighbor.f = i_neighbor.g + i_neighbor.h
                    if i_neighbor not in self.closed_set:
                        heapq.heappush(self.open_set, i_neighbor)
                        self.closed_set.add(i_neighbor)
import import_data as dt
import timeit
from cell import Cell
from astar import AStar
obstacle_lst = dt.data['obstacles']
raw_start = dt.data['bot']
raw_coin = dt.data['coin']
coin = Cell(raw_coin[0], raw_coin[1])
start = Cell(raw_start[0], raw_start[1])
grid_height = dt.data['height']
grid_width = dt.data['width']
#initialize grid
grid = []
for row in range(grid_height):
    a = []
    for col in range(grid_width):
        a.append(0)
    grid.append(a)
#initialize obstacle in the grid
for item in obstacle_lst:
    i = item[0]
    j = item[1]
    grid[i][j] = -1
#initialize coin in the grid
i = coin.x
j = coin.y
grid[i][j] = 'x'
#initialize bot in the grid
i = start.x
j = start.y
grid[i][j] = 's'
shortest_path = AStar(start, coin).find_shortest_path(grid)
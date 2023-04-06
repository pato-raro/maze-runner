import import_data as dt
import timeit
from cell import Cell
from astar import AStar
obstacle_lst = dt.data['obstacles']
bot_lst = dt.data['bots']
start1 = bot_lst[0]['pos']
start2 = bot_lst[1]['pos']
coin = dt.data['coin']
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
i = coin[0]
j = coin[1]
grid[i][j] = 'x'
#initialize bot in the grid
i = start1[0]
j = start1[1]
grid[i][j] = 's1'
i = start2[0]
j = start2[1]
grid[i][j] = 's2'
bot_1 = bot_lst[0]['name']
bot_2 = bot_lst[1]['name']
shortest_path = AStar(bot_1, start1, coin).find_shortest_path(grid)
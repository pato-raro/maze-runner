import time
import import_data as dt
class Cell:
    parent = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = "Unvisited"
    def coor(self):
        return [self.x, self.y]
    '''def get_x(self):
        return self.x
    def get_y(self):
        return self.y'''
    def is_blocked(self, g):
        if g[self.x][self.y] == -1:
            return True
        return False
    def is_valid(self, gridheight, gridwidth):
        if self.x < 0 or self.x >= gridheight or self.y < 0 or self.y >= gridwidth:
            return False
        return True
    def check_goal(self, goal):
        if self.x == goal.x and self.y == goal.y:
            return True
        return False
    def update_neighbors(self, grid):
        self.neighbors = []
        cur = Cell(self.x, self.y)
        if cur.is_valid(dt.data['height'], dt.data['width']):
            neighbor = Cell(cur.x + 1, cur.y)
            if neighbor.is_valid(dt.data['height'], dt.data['width']) and not neighbor.is_blocked(grid): ##right
                self.neighbors.append(neighbor.coor())
            neighbor = Cell(cur.x - 1, cur.y)
            if neighbor.is_valid(dt.data['height'], dt.data['width']) and not neighbor.is_blocked(grid): ##left
                self.neighbors.append(neighbor.coor())
            neighbor = Cell(cur.x, cur.y + 1)
            if neighbor.is_valid(dt.data['height'], dt.data['width']) and not neighbor.is_blocked(grid):#down
                self.neighbors.append(neighbor.coor())
            neighbor = Cell(cur.x, cur.y - 1)
            if neighbor.is_valid(dt.data['height'], dt.data['width']) and not neighbor.is_blocked(grid):#up
                self.neighbors.append(neighbor.coor())  
obstacle_lst = dt.data['obstacles']
raw_start = dt.data['bot']
raw_coin = dt.data['coin']
coin = Cell(raw_coin[0], raw_coin[1])
start = Cell(raw_start[0], raw_start[1])
grid_height = dt.data['height']
grid_width = dt.data['width']
queue = [] ## store unvisited cells
visited = [] ##store visited cells
path = []
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

def InsertPath(pos, queue, visited, path):
    for i_neighbor in pos.neighbors:
        neighbor = Cell(i_neighbor[0], i_neighbor[1])
            ##print(neighbor.coor())
        neighbor.parent = pos
            ##print(neighbor.parent.coor())
        if neighbor.parent.coor() not in path:
            path.append(neighbor.parent.coor())
        if neighbor.coor() not in queue and neighbor.coor() not in visited:
            if not neighbor.check_goal(coin):
                queue.append([neighbor.x, neighbor.y])
                visited.append([neighbor.x, neighbor.y])
            else:
                if neighbor.parent.coor() not in path:
                    path.append([neighbor.parent.x, neighbor.parent.y])
                return 1
def CreatePath(grid, start, coin, queue, visited, path):
    queue.append([start.x, start.y])
    visited.append([start.x, start.y])
    start.parent = None
    if start.coor() == coin.coor():
        return start.coor()
    else:
        while len(queue) > 0:
            pos = [queue.pop(0)]
            temp = Cell(pos[0][0], pos[0][1])
            temp.update_neighbors(grid)
            if InsertPath(temp, queue, visited, path):
                path.append([coin.x, coin.y])
                return path
def checkLength(path,spath,pivot):
    for item in reversed(path):
        length = abs(pivot[0] - item[0]) + abs(pivot[1] - item[1])
        if length == 0:
            spath.insert(0,[pivot[0], pivot[1]])
        elif length == 1:
            spath.insert(0,[item[0], item[1]])
            pivot = item
def FindShortestPath(path):
    spath = []
    pivot = path[len(path) - 1]
    #print(path[len(path) - 1])
    checkLength(path,spath,pivot)
    return spath

def ConvertToStep(path):
    convertedPath = []
    for idx, step in list(enumerate(path)):

        if step == path[-1]:
            break
        # current [3, 2] vs [4, 2]
        if step[0] < path[idx+1][0]:
            convertedPath.append("down")
        if step[0] > path[idx+1][0]:
            convertedPath.append("up")

        # [3, 2] vs [3,3]
        if step[1] < path[idx+1][1]:
            convertedPath.append("right")
        if step[1] > path[idx+1][1]:
            convertedPath.append("left")
    return convertedPath

def WriteToText(context,filename="action.txt"):
    context = "\n".join(context)
    print(context, type(context))
    f = open(filename, "w")
    f.write(context)
    f.close()


#########
path = CreatePath(grid, start, coin, queue, visited, path)

print("This is all the paths that the bot've gone to:")
print(path)

print("This is the shortest path:")
shortestPathCoor = FindShortestPath(path)
shortestPathStep = ConvertToStep(shortestPathCoor)
print(shortestPathCoor)
print(shortestPathStep)

print("Saving into action.txt")

WriteToText(shortestPathStep)





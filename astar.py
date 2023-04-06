import heapq
import timeit
from cell import Cell
class AStar:
    def __init__(self, name, start, coin):
        self.start = Cell(start[0], start[1])
        self.coin = Cell(coin[0], coin[1])
        self.open_set = []
        self.closed_set = set()
        self.path = []
        self.name = name
        self.start_time = timeit.default_timer()
    def convert_to_step(self, path):
        convertedPath = []
        for idx, step in list(enumerate(path)):
            if step == path[-1]:
                break
            # current [3, 2] vs [4, 2]
            if step[0] < path[idx+1][0]:
                stop_time = timeit.default_timer()
                convertedPath.append(["down", (stop_time - self.start_time)*1000])
            if step[0] > path[idx+1][0]:
                stop_time = timeit.default_timer()
                convertedPath.append(["up", (stop_time - self.start_time)*1000])
            # [3, 2] vs [3,3]
            if step[1] < path[idx+1][1]:
                stop_time = timeit.default_timer()
                convertedPath.append(["right", (stop_time - self.start_time)*1000])
            if step[1] > path[idx+1][1]:
                stop_time = timeit.default_timer()
                convertedPath.append(["left", (stop_time - self.start_time)*1000])
        return convertedPath
    def write_to_text(self, content, filename = 'action.txt'):
        filename = self.name +'.txt'
        f = open(filename, "w")
        for item in content:
            f.write(item[0])
            f.write(' ')
            f.write(str(item[1]))
            f.write('\n')
        f.close()
    def find_shortest_path(self, grid):
        self.open_set.append(self.start)
        self.closed_set.add(self.start)
        self.start.g = 0
        self.start.h = self.start.heuristic(self.coin)
        if self.start.coor() == self.coin.coor():
            return self.start.coor()
        while self.open_set:
            cur_pos = heapq.heappop(self.open_set)
            cur_pos.update_neighbors(grid)
            if cur_pos == self.coin:
                while cur_pos is not None:
                    self.path.append(cur_pos.coor())
                    cur_pos = cur_pos.parent
                step = self.convert_to_step(self.path[::-1])
                self.write_to_text(step)
                return self.path[::-1]
            for i_neighbor in cur_pos.neighbors:
                temp_g = cur_pos.g + 1
                if temp_g < i_neighbor.g:
                    i_neighbor.parent = cur_pos
                    i_neighbor.g = temp_g
                    i_neighbor.h = i_neighbor.heuristic(self.coin)
                    i_neighbor.f = i_neighbor.g + i_neighbor.h
                    if i_neighbor not in self.closed_set:
                        heapq.heappush(self.open_set, i_neighbor)
                        self.closed_set.add(i_neighbor)
import heapq
class AStar:
    def __init__(self, start, coin):
        self.start = start
        self.coin = coin
        self.open_set = []
        self.closed_set = []
        self.path = []
    def convert_to_step(self, path):
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
    def write_to_text(self, content, filename = 'action.txt'):
        content = "\n".join(content)
        print(content)
        f = open(filename, "w")
        f.write(content)
        f.close()
    def find_shortest_path(self, grid):
        self.open_set.append(self.start)
        self.closed_set.append(self.start)
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
                        self.closed_set.append(i_neighbor)
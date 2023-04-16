from bot_utils import *
class Map:
    def __init__(self,data):
        self.height = data['height']
        self.width = data['width']
        self.obstacles = data['obstacles']
        self.map = []
        for row in range(self.height):
            a = []
            for col in range(self.width):
                 a.append(0)
            self.map.append(a)
        for item in self.obstacles:
            i = item[0]
            j = item[1]
            self.map[i][j] = -1
    def update_map(self, data):
        for row in range(self.height):
            a = []
            for col in range(self.width):
                 a.append(0)
            self.map.append(a)
        for item in self.obstacles:
            i = item[0]
            j = item[1]
            self.map[i][j] = -1

    

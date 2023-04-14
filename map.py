from bot_utils import *
class Map:
    def __init__(self):
        self.height = import_dt(input_file)['height']
        self.width = import_dt(input_file)['width']
        self.obstacles = import_dt(input_file)['obstacles']
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

    

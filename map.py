import heapq
import json
import math
import os
from typing import List

from location import Location


class Map:
    def __init__(self):
        self.width = None
        self.height = None
        self.obstacles = []
        self.bot = None
        self.coin = None
        self.locations = []
        self.map = []
        self.filename = 'output.txt'
        self.init_file()
        self.load_json()
        self.load_locs()
        self.load_map()
        self.print_map()

    def init_file(self):
        with open(self.filename, 'w') as f:
            pass

    def load_json(self):
        with open('package.json', 'r') as f:
            data = json.load(f)
        self.width = data['width']
        self.height = data['height']
        self.obstacles = [Location(*loc) for loc in sorted(data['obstacles'], key=lambda x: (x[0], x[1]))]
        self.bot = Location(*data['bot'])
        self.coin = Location(*data['coin'])
        self.obstacles = Location.sort(self.obstacles)

    def load_locs(self):
        self.locations = self.obstacles.copy()
        self.locations.append(self.bot)
        self.locations.append(self.coin)

    def load_map(self):
        self.map = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for loc in self.obstacles:
            self.map[loc.x][loc.y] = '*'
        self.map[self.coin.x][self.coin.y] = 'o'
        self.map[self.bot.x][self.bot.y] = 'X'

    def print_map(self):
        print('*' * (self.width + 2))
        for i in range(self.height):
            print('*', end='')
            for j in range(self.width):
                print('{}'.format(self.map[i][j]), end='')
            print('*', end='')
            print()
        print('*' * (self.width + 2))

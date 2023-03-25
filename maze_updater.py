import json
import random
from typing import List
import os
import argparse

class Location:
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def toList(self):
        return [self.x, self.y]
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return True


class Map:
    def __init__(self, fileTXT, fileJSON):
        self.pathInput = fileTXT
        self.pathOutput = fileJSON
        self.loadJson()
        self.inputDirection = self.getInput()
    pathInput = None
    pathOutput = None
    width = None
    height = None
    obstacles: List[Location] = None
    bot: Location = None
    coin: Location = None
    locations = None
    map = None
    inputDirection = None

    def getInput(self):
        filepath = os.path.join(os.getcwd(), self.pathInput)
        with open(filepath, 'r') as f:
            dataInput = f.readlines()
        dataInput = [line.replace("\n", "") for line in dataInput]
        return dataInput

    def loadJson(self):
        path = os.path.join(os.getcwd(), self.pathOutput)
        with open(path, 'r') as file:
            data = json.load(file)
            self.width = data['width']
            self.height = data['height']
            self.obstacles = data['obstacles']
            self.obstacles = [Location(obstacle[0], obstacle[1]) for obstacle in self.obstacles]
            self.bot = Location(data['bot'][0], data['bot'][1])
            self.coin = Location(data['coin'][0], data['coin'][1])
            # self.obstacles = Location.sort(self.obstacles)

    def getMapJSONAsDict(self):
        return {
            'width': self.width,
            'height': self.height,
            'obstacles': [obstacle.toList() for obstacle in self.obstacles],
            'bot': self.bot.toList(),
            'coin': self.coin.toList()
        }

    def random_coin_location(self):
        while True:
            # Chọn vị trí ngẫu nhiên của đồng xu
            coin_position = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]

            # Kiểm tra vị trí của đồng xu không trùng với vị trí của bot
            if coin_position == self.bot.toList():
                break
            # Kiểm tra vị trí của đồng xu không trùng với vị trí của vật cản
            if coin_position in [obstacle.toList() for obstacle in self.obstacles]:
                break
            # Trả về vị trí hợp lệ của đồng xu
            self.coin = Location(coin_position[0], coin_position[1])

    def writeMapAsJSON(self, path, data=''):
        if (data ==''):
            data = {
                'width': self.width,
                'height': self.height,
                'obstacles': [obstacle.toList() for obstacle in self.obstacles],
                'bot': self.bot.toList(),
                'coin': self.coin.toList()
            }
        with open(path, 'w') as file:
            json.dump(data, file)

    def printMapJSONAsDict(self):
        print(self.getMapJSONAsDict())


def updatePos(direction, map):
    mapAsDict = map.getMapJSONAsDict()
    currentPosX, currentPosY = mapAsDict['bot'][0], mapAsDict['bot'][1]
    currentPosX = currentPosX + (1 if direction == 'down' else -1 if direction == 'up' else 0)
    currentPosY = currentPosY + (1 if direction == 'right' else -1 if direction == 'left' else 0)
    map.bot = Location(currentPosX, currentPosY)
    return map

def getPathInp_Out():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', type=str,
                        help='an integer for the accumulator')
    parser.add_argument('-o', type=str,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    if args.i == None or args.o == None:
        print('Please provide the path input, output as following format: python app.py -i "input.txt" -o "output.txt"')
        raise
    return {'input': str(args.i), 'output': str(args.o)}

if __name__ == "__main__":
    path = getPathInp_Out()
    myMap = Map(path['input'], path['output'])
    renderMap = []
    inputDirection = myMap.getInput()
    for direction in inputDirection:
        newPos = updatePos(direction, myMap)
        renderMap.append(myMap.getMapJSONAsDict())
    myMap.printMapJSONAsDict()
    myMap.writeMapAsJSON('maze_render.json', renderMap)
    myMap.random_coin_location()
    myMap.writeMapAsJSON('maze_metadata.json')
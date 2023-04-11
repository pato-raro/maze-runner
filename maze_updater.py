import json
import random
import os
import time
import argparse


class Map:
    def __init__(self, fileTxt1, fileTxt2, fileJSON):
        self.pathInputBot1 = fileTxt1
        self.pathInputBot2 = fileTxt2
        nameBot1 = fileTxt1.replace(".txt", "")
        nameBot2 = fileTxt2.replace(".txt", "")
        self.pathOutput = fileJSON
        try:
            self.loadJson()
        except json.decoder.JSONDecodeError:
            print("MAY BE SOMETHING NOT TRUE...")
            time.sleep(0.01)
            self.loadJson()

        inputDirectionBot1 = self.getInput(self.pathInputBot1)[
            0].strip().split(" ")
        inputDirectionBot1.append(nameBot1)
        inputDirectionBot2 = self.getInput(self.pathInputBot2)[
            0].strip().split(" ")
        inputDirectionBot2.append(nameBot2)
        self.input = [inputDirectionBot1, inputDirectionBot2]

    def update_metadata(self):
        self.setAllBotStop()
        orderUpdate = sorted(self.input, key=lambda x: float(x[1]))
        print(orderUpdate)

        time.sleep(float(orderUpdate[0][1])/1000)
        self.updateBot(orderUpdate[0][2], orderUpdate[0][0])
        print(self.allBotLocation(orderUpdate[0][2]))
        if self.checkEatCoin():
            self.random_coin_location()
        if self.botLocation(orderUpdate[0][2]) in self.allBotLocation(orderUpdate[0][2]):
            self.setBotEliminated(orderUpdate[0][2])
        self.scoreBot()

        time.sleep((float(orderUpdate[1][1])-float(orderUpdate[0][1])) / 1000)
        self.updateBot(orderUpdate[1][2], orderUpdate[1][0])
        if self.checkEatCoin():
            self.random_coin_location()
        print(self.allBotLocation(orderUpdate[1][2]))
        if self.botLocation(orderUpdate[1][2]) in self.allBotLocation(orderUpdate[1][2]):
            self.setBotEliminated(orderUpdate[1][2])
        self.scoreBot()
        self.setAllBotMove()
        self.switchScreenToFalse()

    def updateBot(self, name, direction):
        for index in range(len(self.bots)):
            print(len(self.bots))
            print(self.bots)
            print(self.bots[index]['status'])
            if self.bots[index]['name'] == name and self.bots[index]['status'] != 'eliminated':
                if direction == 'up':
                    self.bots[index]['pos'] = [self.bots[index]
                                               ['pos'][0], self.bots[index]['pos'][1] - 1]
                if direction == 'down':
                    self.bots[index]['pos'] = [self.bots[index]
                                               ['pos'][0], self.bots[index]['pos'][1]+1]
                if direction == 'left':
                    self.bots[index]['pos'] = [self.bots[index]
                                               ['pos'][0] - 1, self.bots[index]['pos'][1]]
                if direction == 'right':
                    self.bots[index]['pos'] = [self.bots[index]
                                               ['pos'][0] + 1, self.bots[index]['pos'][1]]

    def allBotLocation(self, without):
        return [bot['pos'] if bot['name'] != without else "" for bot in self.bots]

    def botLocation(self, name):
        for bot in self.bots:
            if bot['name'] == name:
                return bot['pos']

    def getInput(self, filepath):
        with open(filepath, 'r') as f:
            dataInput = f.readlines()
        dataInput = [line.replace("\n", "") for line in dataInput]
        return dataInput

    def checkEatCoin(self):
        for bot in self.bots:
            if bot['pos'] == self.coin:
                self.random_coin_location()

    def random_coin_location(self):
        coin_position = [random.randint(
            0, self.height - 1), random.randint(0, self.width - 1)]
        while coin_position in self.bots or coin_position in self.obstacles:
            coin_position = [random.randint(
                0, self.height - 1), random.randint(0, self.width - 1)]
        self.coin = [coin_position[0], coin_position[1]]

    def loadJson(self):
        data = None
        path = os.path.join(os.getcwd(), self.pathOutput)
        with open(path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
            self.width = data['width']
            self.height = data['height']
            self.obstacles = data['obstacles']
            self.bots = data['bots']
            self.coin = data['coin']
            self.screen = data['screen']

    def getMapJSONAsDict(self):
        return {
            'width': self.width,
            'height': self.height,
            'obstacles': self.obstacles,
            'bots': self.bots,
            'coin': self.coin,
            'screen': self.screen
        }

    def writeMapAsJSON(self, path, data=''):
        if (data == ''):
            data = {
                'width': self.width,
                'height': self.height,
                'obstacles': self.obstacles,
                'bots': self.bots,
                'coin': self.coin,
                'screen': self.screen
            }
        with open(path, 'w') as file:
            json.dump(data, file)

    def scoreBot(self):
        for bot in self.bots:
            if bot['pos'] == self.coin:
                bot['score'] += 1

    def setAllBotStop(self):
        for bot in self.bots:
            bot['status'] = "stop" if bot['status'] != "eliminated" else "eliminated"

    def setAllBotMove(self):
        for bot in self.bots:
            bot['status'] = "move"

    def setBotEliminated(self, botName):
        for index in range(len(self.bots)):
            if self.bots[index]['name'] == botName:
                self.bots[index]['status'] = "eliminated"

    def switchScreenToFalse(self):
        self.screen = False

    def readScreen(self):
        return self.screen

    def printMapJSONAsDict(self):
        print(self.getMapJSONAsDict())


def getPathInp_Out():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', type=str, action="append", nargs='+')
    parser.add_argument('-o', type=str)
    args = parser.parse_args()
    if args.i == None or args.o == None:
        print('Please provide the path input, output as following format: python app.py -i "input.txt" -o "output.txt"')
        raise
    return {'input': [item[0] for item in args.i], 'output': str(args.o)}


def update():
    path = getPathInp_Out()
    while True:
        time.sleep(2)
        myMap = None
        myMap = Map(path['input'][0], path['input'][1], path['output'])
        # print(myMap.readScreen())
        if myMap.readScreen() == True:
            myMap.printMapJSONAsDict()
            myMap.update_metadata()
            myMap.writeMapAsJSON('maze_metadata.json')
        else:
            continue


if __name__ == "__main__":
    update()

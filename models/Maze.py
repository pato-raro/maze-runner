import pygame
import random
from utils.helper import drawMaze, getJsonData
from utils.constants import CELL_SIZE, MAP_IMAGE, COIN_IMAGE_LIST, OBSTACLE_IMAGE, HEADER_HEIGHT, HEADER_IMAGE
from .Bot import Bot


class Maze:
    def __init__(self, maze_metadata, ballStar):
        self.maze = getJsonData(maze_metadata)
        self.config = {
            'headerImage': HEADER_IMAGE,
            'headerHeight': HEADER_HEIGHT,
            'size': CELL_SIZE,
            'background': MAP_IMAGE,
            'coinImage': COIN_IMAGE_LIST[ballStar],
            'obstacleImage': OBSTACLE_IMAGE,
        }

    def initBotList(self):
        botList = self.maze['bots']
        self.botList = []
        imageList = ['./assets/images/goku.png',
                     './assets/images/vegeta.png']

        killSoundList = ['./assets/voices/kill.mp3',
                         './assets/voices/muda.mp3']
        deathSoundList = ['./assets/voices/yamete.mp3',
                          './assets/voices/eh.mp3']

        for bot in botList:
            botIndex = botList.index(bot)
            name, location, status, score = bot.values()

            if status != "eliminated":
                player = Bot(name, location, status, score)
                player.setImage(imageList[botIndex])
                player.setVoices(killSoundList[botIndex], deathSoundList[botIndex])
                self.botList.append(player)

    def render(self, surface, botScores, elapsedTime):
        drawMaze(surface, self.maze, self.config,
                 self.botList, botScores, elapsedTime)
        self.maze["screen"] = True
        pygame.display.flip()

    def randomNewCoin(self):
        rowLimit = self.maze["height"] - 1
        colLimit = self.maze["width"] - 1
        obstacleList = self.maze["obstacles"]

        newLocation = [random.randint(
            0, rowLimit), random.randint(0, colLimit)]

        while newLocation in obstacleList:
            newLocation = [random.randint(
                0, rowLimit), random.randint(0, colLimit)]

        self.maze["coin"] = newLocation

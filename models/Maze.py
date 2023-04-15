import pygame
import random
from utils.helper import drawMaze, getJsonData
from utils.constants import CELL_SIZE, MAP_IMAGE, COIN_IMAGE_LIST, OBSTACLE_IMAGE, HEADER_HEIGHT
from .Bot import Bot


class Maze:
    def __init__(self, maze_metadata, ballStar):
        self.maze = getJsonData(maze_metadata)
        self.config = {
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

        killSoundList = ['./assets/sounds/kill.mp3',
                         './assets/sounds/muda.mp3']
        deathSoundList = ['./assets/sounds/yamete.mp3',
                          './assets/sounds/eh.mp3']

        for bot in botList:
            botIndex = botList.index(bot)
            name, location, status, score = bot.values()

            player = Bot(name, location, status, score)
            if status == "eliminated":
                player.setEliminatedImage('./assets/images/death.gif')
            player.setImage(imageList[botIndex])
            player.setVoices(killSoundList[botIndex], deathSoundList[botIndex])
            self.botList.append(player)

    def render(self, surface, elapsedTime):
        drawMaze(surface, self.maze, self.config,
                 self.botList, elapsedTime)
        self.maze["screen"] = True
        pygame.display.update()

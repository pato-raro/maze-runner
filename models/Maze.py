import pygame
from utils.helper import drawMaze, getJsonData
from utils.constants import CELL_SIZE, BOARD_SIZE, MAP_IMAGE, COIN_IMAGE, OBSTACLE_IMAGE
from .Bot import Bot


class Maze:
    def __init__(self, maze_metadata):
        self.maze = getJsonData(maze_metadata)
        self.config = {
            'size': CELL_SIZE,
            'background': MAP_IMAGE,
            'coinImage': COIN_IMAGE,
            'obstacleImage': OBSTACLE_IMAGE,
        }
        self.window = pygame.display.set_mode(BOARD_SIZE)

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

            if status == "eliminated":
                continue

            player = Bot(name, location, status, score)
            player.setImage(imageList[botIndex])
            player.setVoices(killSoundList[botIndex], deathSoundList[botIndex])
            self.botList.append(player)

    def render(self):
        drawMaze(self.window, self.maze, self.config, self.botList)

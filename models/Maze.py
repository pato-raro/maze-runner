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
        self.botList = []

    def initBotList(self):
        characterList = self.maze['bots']
        imageList = ['./assets/images/goku.png',
                     './assets/images/vegeta.png']

        killSoundList = ['./assets/voices/kill.mp3',
                         './assets/voices/muda.mp3']
        deathSoundList = ['./assets/voices/yamete.mp3',
                          './assets/voices/eh.mp3']

        for character in characterList:
            charIndex = characterList.index(character)
            name, location, status, score = character.values()
            bot = Bot(name, location, status, score)
            bot.setImage(imageList[charIndex])
            bot.setVoices(killSoundList[charIndex], deathSoundList[charIndex])
            self.botList.append(bot)

    def render(self):
        drawMaze(self.window, self.maze, self.config, self.botList)

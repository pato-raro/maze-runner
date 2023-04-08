import os
import random
import pygame
from .Maze import Maze
from time import sleep
from utils.constants import WINDOW
from utils.helper import setJsonData


class GameBoard:
    def __init__(self, filePath):
        self.filePath = filePath
        self.actionList = ['actions/tadao.txt', 'actions/top.txt']
        self.modifiedOn = os.path.getmtime(filePath)

    def initGame(self, ballStar):
        self.board = Maze(self.filePath, ballStar)
        self.board.initBotList()
        self.board.render(WINDOW)

    def start(self):
        ballStar = 0
        self.initGame(ballStar)
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            sleep(0.2)
            modified = os.path.getmtime(self.filePath)

            coinLocation = self.board.maze["coin"]

            if modified != self.modifiedOn:
                self.modifiedOn = modified
                self.initGame(ballStar)
                print("Re-render")
            for bot in self.board.botList:
                if bot.location == coinLocation:
                    self.board.randomNewCoin()
                    setJsonData(self.filePath, self.board.maze)
                    ballStar = random.randint(0, 6)

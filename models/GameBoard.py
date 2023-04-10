import os
import random
import pygame
from .Maze import Maze
from utils.constants import WINDOW
from utils.helper import setJsonData


class GameBoard:
    def __init__(self, filePath):
        self.filePath = filePath
        self.actionList = ['actions/tadao.txt', 'actions/top.txt']

    def initGame(self, ballStar):
        self.board = Maze(self.filePath, ballStar)
        self.board.initBotList()

    def start(self):
        ballStar = 0
        self.initGame(ballStar)
        self.board.render(WINDOW, ballStar, {
                          bot.name: bot.score for bot in self.board.botList})
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            coinLocation = self.board.maze["coin"]

            self.initGame(ballStar)
            if self.board.maze["screen"] == False:
                self.board.render(WINDOW, ballStar, {
                                    bot.name: bot.score for bot in self.board.botList})
                setJsonData(self.filePath, self.board.maze)

            for bot in self.board.botList:
                if bot.location == coinLocation:
                    ballStar = random.randint(0, 6)
                    self.board.randomNewCoin()
                    setJsonData(self.filePath, self.board.maze)

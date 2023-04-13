import os
import random
import pygame
import asyncio
from .Maze import Maze
from utils.constants import WINDOW
from utils.helper import setJsonData,renderTime
import time


class GameBoard:
    def __init__(self, filePath): # khởi tạo đối tượng gameboard
        self.filePath = filePath
        self.actionList = ['actions/tadao.txt', 'actions/top.txt']

    def initGame(self, ballStar): # khởi tạo trò chơi
        self.board = Maze(self.filePath, ballStar)
        self.board.initBotList()

    def start(self):
        ballStar = 0
        timeLimit = 80       # minutes
        self.initGame(ballStar)
        self.board.render(WINDOW, {
                          bot.name: bot.score for bot in self.board.botList}, timeLimit)         
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            total_mins = timeLimit//60 # minutes left
            total_sec = timeLimit-(60*(total_mins)) #seconds left
            timeLimit -= 1
            if timeLimit > -1:
                font = pygame.font.SysFont('freesansbold.ttf', 25)
                text = font.render(("elapseTime: "+str(total_mins)+":"+str(total_sec)), True, 'red')
                WINDOW.blit(text, (400, 400))
                pygame.display.flip()
                time.sleep(1)#making the time interval of the loop 1sec
            else:
                font = pygame.font.SysFont('freesansbold.ttf', 25)
                text = font.render("Time Over!!", True, 'red')
                WINDOW.blit(text, (360, 60))
                pygame.display.flip()
            coinLocation = self.board.maze["coin"]

            self.initGame(ballStar)
            if self.board.maze["screen"] == False:
                self.board.render(WINDOW,  {
                    bot.name: bot.score for bot in self.board.botList}, timeLimit)
                setJsonData(self.filePath, self.board.maze)

            for bot in self.board.botList:
                if bot.location == coinLocation:
                    ballStar = random.randint(0, 6)
                    self.board.randomNewCoin()
                    setJsonData(self.filePath, self.board.maze)

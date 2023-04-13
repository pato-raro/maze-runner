import os
import random
import pygame
import asyncio
from .Maze import Maze
from utils.constants import WINDOW , HEADER_SIZE
from utils.helper import setJsonData
import time


class GameBoard:
    def __init__(self, filePath): # khởi tạo đối tượng gameboard
        self.filePath = filePath
        self.actionList = ['actions/tadao.txt', 'actions/top.txt']

    def initGame(self, ballStar): # khởi tạo trò chơi
        self.board = Maze(self.filePath, ballStar)
        self.board.initBotList()

    def countDown():
        done =  False
        secs = 0
        mins= 0
        font = pygame.font.SysFont('freesansbold.ttf',32)
        text = font.render("{}:{}".format(mins,secs),True,'red','green')
        textRect = text.get_rect()
        text
    def start(self):
        ballStar = 0
        timeLimit = 90       # seconds
        self.initGame(ballStar)
        self.board.render(WINDOW, {
                          bot.name: bot.score for bot in self.board.botList}, timeLimit)         
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            total_mins = timeLimit//60 # minutes left
            total_secs = timeLimit-(60*(total_mins)) #seconds left
            timeLimit -= 1
            if total_secs == 0:
                total_secs= 60
                total_mins-= 1
            if timeLimit > -1:
                font = pygame.font.SysFont('freesansbold.ttf', 25)
                text = font.render("{}:{}".format(total_mins,total_secs),True,'red','green')
                WINDOW.blit(text, (380, 45))
                pygame.display.flip()
                time.sleep(1)#making the time interval of the loop 1sec
            else:
                font = pygame.font.SysFont('freesansbold.ttf', 25)
                text = font.render("Time Over!!", True, 'red')
                WINDOW.blit(text, (380, 45))
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

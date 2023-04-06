import pygame
import asyncio
from .Maze import Maze


class GameBoard:
    def __init__(self):
        self.board = Maze('maze_metadata.json')
        self.actionList = ['actions/tadao.txt', 'actions/top.txt']

    def initGame(self):
        self.board.initBotList()

        botList = self.board.botList

        for bot in botList:
            index = botList.index(bot)
            bot.setMoves(self.actionList[index])

        self.board.render()

    async def start(self):
        botList = self.board.botList

        running = True
        while running:
            global botMoveTask
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for bot in botList:
                if len(bot.moveSet) != 0:
                    direction = bot.moveSet.pop(0)
                    botMoveTask = asyncio.create_task(
                        bot.move(direction, 0.2, self.board.render))
            await botMoveTask

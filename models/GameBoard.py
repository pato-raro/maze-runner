import pygame
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

    def start(self):
        botList = self.board.botList

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for bot in botList:
                if bot.status != "move":
                    continue

                if len(bot.moveSet) != 0:
                    move = bot.moveSet.pop(0)
                    bot.move(move["direction"], float(
                        move["time"]), self.board.render)

                if bot.isOver:
                    botIndex = botList.index(bot)
                    botList.pop(botIndex)
                    bot.gameOver()

                if bot.name == "tadao":
                    bot.isOver = True

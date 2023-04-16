import random
import pygame
from .Maze import Maze
from .Maze import Maze
from utils.constants import WINDOW, BOARD_SIZE, CLOCK, FPS, TIME_LIMIT
from utils.helper import setJsonData, renderText


class GameBoard:
    def __init__(self, filePath):  # khởi tạo đối tượng gameboard
        self.filePath = filePath
        self.background_sound = pygame.mixer.Sound(
            './assets/sounds/Pixelland.wav')
        self.timeLeft = TIME_LIMIT  # seconds
        self.isGameOver = False
        self.last_count = pygame.time.get_ticks()

    def initGame(self, ballStar):  # khởi tạo trò chơi
        self.board = Maze(self.filePath, ballStar)
        self.board.initBotList()
        self.winner = self.board.botList[0]
        self.loser = None

    def start(self):
        pygame.mixer.Channel(2).play(self.background_sound, -1)
        self.background_sound.set_volume(0.3)

        ballStar = 0
        self.initGame(ballStar)
        self.board.render(WINDOW, self.timeLeft)
        running = True
        while running:
            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.timeLeft == 0:
                self.isGameOver = True

            self.countdown()
            if not self.isGameOver:
                coinLocation = self.board.maze["coin"]
                self.initGame(ballStar)

                if self.board.maze["screen"] == False:
                    self.board.render(WINDOW, self.timeLeft)
                    setJsonData(self.filePath, self.board.maze)

                for bot in self.board.botList:
                    if bot.score > self.winner.score:
                        self.winner = bot
                    if bot.location == coinLocation:
                        ballStar = random.randint(0, 6)
                        print(ballStar)

                    if bot.status == "eliminated":
                        bot.gameOver()
                        self.loser = bot
                        self.winner = next(
                            x for x in self.board.botList if x.name != bot.name)
                        self.isGameOver = True
                        break

            else:
                if self.loser != None:
                    running = False
                    self.gameOver(0)
                else:
                    highest_score_bot = 0
                    for bot in self.board.botList:
                        if bot.score == self.winner.score:
                            highest_score_bot += 1
                    running = False
                    self.gameOver(highest_score_bot)

    def countdown(self):
        total_mins = int(self.timeLeft//60)  # minutes left
        total_secs = self.timeLeft-((60*(total_mins)))  # seconds left

        text_color = 'black'

        if self.timeLeft <= 5:
            text_color = 'red'

        if self.timeLeft > 0:
            font = pygame.font.SysFont('freesansbold.ttf', 25)
            text = font.render(
                (f"{total_mins:02}:{total_secs:02}"), True, text_color, 'white')

            count_timer = pygame.time.get_ticks()
            if count_timer - self.last_count > 1000:
                self.timeLeft -= 1
                self.last_count = count_timer

            WINDOW.blit(text, (380, 42))
            pygame.display.flip()
        else:
            font = pygame.font.SysFont('freesansbold.ttf', 25)
            text = font.render("Time Over!!", True, text_color, 'white')
            WINDOW.blit(text, (355, 42))
            pygame.display.flip()

    def gameOver(self, highest_score_bot):
        winner = self.winner.name if self.winner != None else ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return self.reset_game()

            s = pygame.Rect(0, 0, 300, 150)
            s.center = tuple(x // 2 for x in BOARD_SIZE)
            pygame.draw.rect(WINDOW, pygame.Color("#ffffff80"), s)

            if highest_score_bot < 2:
                renderText(WINDOW, f"{winner} wins!", s.centerx,
                           s.centery - 20, 32, center=True)
            elif highest_score_bot == 2:
                renderText(WINDOW, "It's a draw!", s.centerx,
                           s.centery - 20, 32, center=True)
            renderText(WINDOW, "Press 'Enter' to restart game!",
                       s.centerx, s.centery + 20, 24, center=True)
            pygame.display.update()

    def reset_game(self):
        width, height, obstacles, bots, coin, screen = self.board.maze.values()
        for bot in bots:
            bot["score"] = 0
        reset_maze = {
            "width": width,
            "height": height,
            "obstacles": obstacles,
            "bots": bots,
            "coin": coin,
            "screen": screen,
        }
        self.timeLeft = TIME_LIMIT
        self.isGameOver = False
        setJsonData(self.filePath, reset_maze)
        self.start()

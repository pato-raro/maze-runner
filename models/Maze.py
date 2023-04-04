import pygame
from utils.helper import drawMaze, getJsonData
from utils.constants import CELL_SIZE, BOARD_SIZE, MAP_IMAGE, COIN_IMAGE, OBSTACLE_IMAGE, BOT_IMAGE_LIST

class Maze:
    def __init__(self, maze_metadata):
        self.maze = getJsonData(maze_metadata)
        self.config = {
            'size': CELL_SIZE,
            'background': MAP_IMAGE,
            'coinImage': COIN_IMAGE,
            'obstacleImage': OBSTACLE_IMAGE,
            'botImageList': BOT_IMAGE_LIST
        }
        self.window = pygame.display.set_mode(BOARD_SIZE)

    def render(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            drawMaze(self.window, self.maze, self.config)

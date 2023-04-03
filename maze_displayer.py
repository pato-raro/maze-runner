import pygame
from helper import drawMaze, getJsonData
from constants import WINDOW, CELL_SIZE, MAP_IMAGE, COIN_IMAGE, OBSTACLE_IMAGE, BOT_IMAGE_LIST

MAZE = getJsonData('maze_metadata.json')
CONFIG = {
    'size': CELL_SIZE,
    'background': MAP_IMAGE,
    'coinImage': COIN_IMAGE,
    'obstacleImage': OBSTACLE_IMAGE,
    'botImageList': BOT_IMAGE_LIST
}


def render():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawMaze(WINDOW, MAZE, CONFIG)


if __name__ == "__main__":
    render()

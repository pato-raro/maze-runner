import pygame
from helper import getJsonData, getImage

INIT_MAZE = getJsonData('maze_metadata.json')
WIDTH, HEIGHT, OBSTACLES, INIT_BOT, INIT_COIN = INIT_MAZE.values()

CELL_SIZE = 40
BOARD_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
SCALE_RATIO = (CELL_SIZE, CELL_SIZE)

WINDOW = pygame.display.set_mode(BOARD_SIZE)

MAP_IMAGE = getImage('assets/map.png', BOARD_SIZE)
COIN_IMAGE = getImage('assets/coin.png', SCALE_RATIO)
OBSTACLE_IMAGE = getImage('assets/obstacle.png', SCALE_RATIO)
BOT_IMAGE_LIST = list(map(lambda source: getImage(source, SCALE_RATIO), [
                 'assets/vegeta.png', 'assets/goku.png']))
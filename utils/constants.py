import pygame
from .helper import getJsonData, getImage

INIT_MAZE = getJsonData('maze_metadata.json')
WIDTH, HEIGHT, OBSTACLES, INIT_BOT, INIT_COIN, INIT_SCREEN = INIT_MAZE.values()

CELL_SIZE = 40
HEADER_HEIGHT = (2 * CELL_SIZE)
HEADER_SIZE = (WIDTH * CELL_SIZE, HEADER_HEIGHT)
BOARD_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE + HEADER_HEIGHT)
SCALE_RATIO = (CELL_SIZE, CELL_SIZE)

WINDOW = pygame.display.set_mode(BOARD_SIZE)

MAP_IMAGE = getImage('assets/images/map.png', BOARD_SIZE)
OBSTACLE_IMAGE = getImage('assets/images/obstacle.png', SCALE_RATIO)

HEADER_IMAGE = getImage('assets/images/header.jpg', HEADER_SIZE)

COIN_IMAGE_LIST = list(map(lambda source: getImage(source, SCALE_RATIO), [
    'assets/images/one.png',
    'assets/images/two.png',
    'assets/images/three.png',
    'assets/images/four.png',
    'assets/images/five.png',
    'assets/images/six.png',
    'assets/images/seven.png',
]))

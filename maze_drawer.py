import pygame
import json

def load_JSON_file(file_name):
    file = open(file_name + '.json', 'r')
    data = json.loads(file.read())
    file.close()
    return data


INIT_MAZE = load_JSON_file('maze_metadata')

INIT_WIDTH, INIT_HEIGHT, INIT_OBSTACLES, INIT_BOT, INIT_COIN = INIT_MAZE.values()

CELL_SIZE = 40
BOARD_SIZE = (INIT_WIDTH * CELL_SIZE, INIT_HEIGHT * CELL_SIZE)

SCALE = (CELL_SIZE, CELL_SIZE)


def load_image(source, scale):
    ORIGIN_IMAGE = pygame.image.load(source)
    IMAGE = pygame.transform.scale(ORIGIN_IMAGE, scale)
    return IMAGE


BACKGROUND = load_image('assets/background.webp', BOARD_SIZE)
BOT_IMAGE = load_image('assets/Granny.webp', SCALE)
COIN_IMAGE = load_image('assets/R.png', SCALE)
OBSTACLE_IMAGE = load_image('assets/obstacle.jpg', SCALE)

WHITE = (255, 255, 255)


def display(surface, maze):
    # WINDOW.blit(BACKGROUND, (0, 0))
    surface.fill(WHITE)
    WIDTH, HEIGHT, OBSTACLES, BOT, COIN = maze.values()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if [i, j] == BOT:
                surface.blit(BOT_IMAGE, (j * CELL_SIZE, i * CELL_SIZE))
            if [i, j] == COIN:
                surface.blit(COIN_IMAGE, (j * CELL_SIZE, i * CELL_SIZE))
            if [i, j] in OBSTACLES:
                surface.blit(OBSTACLE_IMAGE, (j * CELL_SIZE, i * CELL_SIZE))
    pygame.display.update()

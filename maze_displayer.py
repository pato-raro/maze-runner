import pygame
from maze_drawer import display, load_JSON_file, BOARD_SIZE

WINDOW = pygame.display.set_mode(BOARD_SIZE)


def load_text_file(file_name):
    file = open(file_name + '.txt', 'r')
    data = file.readlines()
    file.close()
    return data


def play():
    from bot import find_path
    find_path()
    ACTION_LIST = load_text_file('action')
    MAZE = load_JSON_file('maze_metadata')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for action in ACTION_LIST:

            BOT = MAZE['bot']
            COIN = MAZE['coin']
            action = action.strip()
            if action == "down":
                BOT[0] += 1
            elif action == "up":
                BOT[0] -= 1
            elif action == "left":
                BOT[1] -= 1
            elif action == "right":
                BOT[1] += 1
            else:
                continue

            pygame.time.wait(200)
            display(WINDOW, MAZE)
            if BOT == COIN:
                return
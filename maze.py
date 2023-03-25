import pygame
import json
import os
from time import sleep
import random

# Clear screen helper


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw maze and display postion of bot and coin


def draw_maze(maze):
    WIDTH, HEIGHT, OBSTACLES, BOT, COIN = maze.values()
    for i in range(-1, HEIGHT + 1):
        for j in range(-1, WIDTH + 1):
            if i == -1 or i == HEIGHT or j == -1 or j == WIDTH:
                print("*", end=" ")
            elif [i, j] in OBSTACLES:
                print("*", end=" ")
            elif [i, j] == BOT:
                print("X", end=" ")
            elif [i, j] == COIN:
                print("O", end=" ")
            else:
                print(" ", end=" ")
        print()


def start_game():
    # Read maze data from file
    file_open = open('maze_metadata.json', 'r')
    maze = json.loads(file_open.read())
    file_open.close()

    WIDTH, HEIGHT, OBSTACLES, *rest = maze.values()

    BOT_POSITION = maze['bot']

    # Draw initial maze
    draw_maze(maze)

    # Invoke the algorithm to get solution steps
    # Mockup solution related with the mockup data
    file_solution = open('action.txt', 'r')
    action_list = file_solution.readlines()
    file_solution.close()

    # Update console screen after 0.5s
    for action in action_list:
        sleep(0.25)
        clear_screen()
        move = action.strip()
        if move == "down":
            BOT_POSITION[0] += 1
        elif move == "up":
            BOT_POSITION[0] -= 1
        elif move == "left":
            BOT_POSITION[1] -= 1
        elif move == "right":
            BOT_POSITION[1] += 1
        else:
            continue
        draw_maze(maze)
        print(action.capitalize())
    print("Done after {} move(s)!".format(len(action_list)))

    # Get new random position of coin
    NEW_COIN_Y = random.randint(0, HEIGHT)
    NEW_COIN_X = random.randint(0, WIDTH)

    # If this coordinate is in obstacle list, do it again
    while ([NEW_COIN_Y, NEW_COIN_X] in maze['obstacles']):
        NEW_COIN_Y = random.randint(0, HEIGHT)
        NEW_COIN_X = random.randint(0, WIDTH)

    NEW_COIN_POSITION = [NEW_COIN_Y, NEW_COIN_X]
    maze_dict = {
        "width": WIDTH,
        "height": HEIGHT,
        "obstacles": OBSTACLES,
        "bot": BOT_POSITION,
        "coin": NEW_COIN_POSITION
    }
    # Overwriting new maze data to update maze_metadata.json file
    json_maze = json.dumps(maze_dict)
    update_maze_file = open('maze_metadata.json', 'w')
    update_maze_file.write(json_maze)
    update_maze_file.close()

    # Call to run recursively until stop command
    # start_game()

if __name__ == "__main__":
    start_game()

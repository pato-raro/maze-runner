import json


def generate_maze(path_file):
    file = open(path_file, 'r')
    row_list = file.readlines()
    file.close()

    HEIGHT = len(row_list)
    WIDTH = len(row_list[0].strip().split(","))
    BOT = []
    COIN = []
    OBSTACLES = []

    for row_index in range(HEIGHT):
        row = row_list[row_index].strip().split(',')
        for col_index in range(WIDTH):
            if row[col_index] == 'X':
                BOT = [row_index, col_index]
            elif row[col_index] == 'O':
                COIN = [row_index, col_index]
            elif row[col_index] == '*':
                OBSTACLES.append([row_index, col_index])
            
    maze_dict = {
        "width": WIDTH,
        "height": HEIGHT,
        "obstacles": OBSTACLES,
        "bot": BOT,
        "coin": COIN
    }
    json_maze = json.dumps(maze_dict)
    update_maze_file = open('maze_metadata.json', 'w')
    update_maze_file.write(json_maze)
    update_maze_file.close()


if __name__ == "__main__":
    generate_maze('maze.csv')

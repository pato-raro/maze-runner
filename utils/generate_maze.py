import json


def generateMaze(pathFile):
    file = open(pathFile, 'r')
    rowList = file.readlines()
    file.close()

    HEIGHT = len(rowList)
    WIDTH = len(rowList[0].strip().split(","))
    BOT = []
    COIN = []
    OBSTACLES = []

    for rowIndex in range(HEIGHT):
        row = rowList[rowIndex].strip().split(',')
        for colIndex in range(WIDTH):
            if row[colIndex] == 'X':
                BOT = [rowIndex, colIndex]
            elif row[colIndex] == 'O':
                COIN = [rowIndex, colIndex]
            elif row[colIndex] == '*':
                OBSTACLES.append([rowIndex, colIndex])

    mazeDictionary = {
        "width": WIDTH,
        "height": HEIGHT,
        "obstacles": OBSTACLES,
        "bots": BOT,
        "coin": COIN
    }
    jsonMaze = json.dumps(mazeDictionary)
    updatedMazeFile = open('maze_metadata.json', 'w')
    updatedMazeFile.write(jsonMaze)
    updatedMazeFile.close()


if __name__ == "__main__":
    generateMaze('maze.csv')

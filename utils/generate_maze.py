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
            if row[colIndex] != '' and row[colIndex] != 'O' and row[colIndex] != '*':
                BOT.append({
                    "name": row[colIndex],
                    "pos": [rowIndex, colIndex],
                    "status": "stop",
                    "score": 0
                })
            elif row[colIndex] == 'O':
                COIN = [rowIndex, colIndex]
            elif row[colIndex] == '*':
                OBSTACLES.append([rowIndex, colIndex])

    mazeDictionary = {
        "width": WIDTH,
        "height": HEIGHT,
        "obstacles": OBSTACLES,
        "bots": BOT,
        "coin": COIN,
        "screen": False
    }
    jsonMaze = json.dumps(mazeDictionary)
    updatedMazeFile = open('maze_metadata.json', 'w')
    updatedMazeFile.write(jsonMaze)
    updatedMazeFile.close()


if __name__ == "__main__":
    generateMaze('./utils/maze.csv')

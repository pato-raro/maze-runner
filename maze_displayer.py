from models.GameBoard import GameBoard

if __name__ == "__main__":
    boardGame = GameBoard('maze_metadata.json')
    boardGame.start()

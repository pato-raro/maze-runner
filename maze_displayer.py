import asyncio
from models.GameBoard import GameBoard

if __name__ == "__main__":
    boardGame = GameBoard()
    boardGame.initGame()
    asyncio.run(boardGame.start())

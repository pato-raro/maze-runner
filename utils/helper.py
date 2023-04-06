import json
import pygame


def getJsonData(pathFile):
    file = open(pathFile, 'r')
    data = json.loads(file.read())
    file.close()
    return data


def getImage(source, scaleRatio):
    originImage = pygame.image.load(source)
    transformImage = pygame.transform.scale(originImage, scaleRatio)
    return transformImage


def drawMaze(surface, maze, config, botList):
    size, background, coinImage, obstacleImage = config.values()
    surface.blit(background, (0, 0))
    # surface.fill((255, 255, 255))
    width, height, obstacles, bots, coin, screen = maze.values()
    botPositionList = list(map(lambda bot: bot.location, botList))
    for i in range(height):
        for j in range(width):
            location = [i, j]
            if location in botPositionList:
                botIndex = botPositionList.index(location)
                surface.blit(botList[botIndex].image, (j * size, i * size))
            if location == coin:
                surface.blit(coinImage, (j * size, i * size))
            if location in obstacles:
                surface.blit(obstacleImage, (j * size, i * size))
    pygame.display.update()

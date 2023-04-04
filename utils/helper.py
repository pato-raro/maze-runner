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

def getVoice(source):
    mixer = pygame.mixer
    mixer.init()
    mixer.music.load(source) 
    mixer.music.set_volume(0.5)
    return mixer


def drawMaze(surface, maze, config):
    size, background, coinImage, obstacleImage, botImageList = config.values()
    surface.blit(background, (0, 0))
    # surface.fill((255, 255, 255))
    width, height, obstacles, botList, coin, screen = maze.values()
    botPositionList = list(map(lambda bot: bot["pos"], botList))
    for i in range(height):
        for j in range(width):
            location = [i, j]
            if location in botPositionList:
                botIndex = botPositionList.index(location)
                surface.blit(botImageList[botIndex], (j * size, i * size))
            if location == coin:
                surface.blit(coinImage, (j * size, i * size))
            if location in obstacles:
                surface.blit(obstacleImage, (j * size, i * size))
    pygame.display.update()

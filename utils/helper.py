import json
import time
import pygame


def getJsonData(pathFile):
    file = open(pathFile, 'r')
    data = json.loads(file.read())
    file.close()
    return data


def setJsonData(pathFile, data):
    file = open(pathFile, 'w')
    jsonData = json.dumps(data)
    file.write(jsonData)
    file.close()


def getImage(source, scaleRatio):
    originImage = pygame.image.load(source)
    transformImage = pygame.transform.scale(originImage, scaleRatio)
    return transformImage


def renderTime(surface, elapsedTime, headerWidth, headerHeight):
    # formatedTime = time.strftime("%M:%S", time.gmtime(elapsedTime * 60))
    # font = pygame.font.SysFont('freesansbold.ttf', 25) # khoi tao font chu
    # time_text = font.render(f'{formatedTime}', True, ('red'))
    # text_rect = time_text.get_rect(
    #     center=(headerWidth // 2, headerHeight // 2))
    color = (0, 0, 0)
    pygame.draw.rect(surface, color, pygame.Rect(headerWidth // 2.35 , headerHeight // 4, 120, 60),  3,  3)


    # surface.blit(time_text, text_rect)

def renderScore(surface, botIndex, bot):
    botName = bot.name
    botScore = bot.score
    botImage = bot.image
    print("name: ", botName, " score: ", botScore)
    color = (0, 0, 0)
    y = 20
    if botIndex % 2 == 0:
        position = "left"
        x = 10
    else:
        position = "right"
        x = 550
    if position == "left":
        pygame.draw.rect(surface, color, pygame.Rect(
            x, y, 240, 60), 3, border_bottom_right_radius=60)

    elif position == "right":
        pygame.draw.rect(surface, color, pygame.Rect(
            x, y, 240, 60), 3, border_bottom_left_radius=60)
        

    pygame.display.flip()


def drawMaze(surface, maze, config, botList, botScores=None, elapsedTime=None):
    headerHeight, size, background, coinImage, obstacleImage = config.values()
    surface.fill('green')
    surface.blit(background, (0, 0 + headerHeight))
    renderTime(surface, elapsedTime, size * maze['width'], headerHeight)
    width, height, obstacles, bots, coin, screen = maze.values()
    botPositionList = list(map(lambda bot: bot.location, botList))
    for i in range(height):
        for j in range(width):
            location = [i, j]
            if location in botPositionList:
                botIndex = botPositionList.index(location)
                renderScore(surface, botIndex, botList[botIndex])
                surface.blit(botList[botIndex].image,
                             (j * size, i * size + headerHeight))
            if location == coin:
                surface.blit(coinImage, (j * size, i * size + headerHeight))
            if location in obstacles:
                surface.blit(obstacleImage, (j * size, i * size + headerHeight))
    pygame.display.flip()

import json
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
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    time_text = font.render(f'Time: {int(elapsedTime)}', True, (0, 0, 0))
    text_rect = time_text.get_rect(center = (headerWidth // 2.6, headerHeight // 2.5))
    surface.blit(time_text, text_rect)
    
def renderScore(surface, botScores,headerWidth,headerHeight):
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    score_text = font.render(f'Scores1: {botScores}', True, ('black'))
    score_rect = score_text.get_rect(center = (headerWidth // 2.6, headerHeight // 1.8))
    surface.blit(score_text, score_rect)



def drawMaze(surface, maze, config, botList, botScores=None, elapsedTime=None):
    headerImage, headerHeight, size, background, coinImage, obstacleImage = config.values()
    #surface.fill((255, 255, 255))
    surface.blit(headerImage, (0, 0))
    surface.blit(background, (0, 0 + headerHeight))
    renderTime(surface, 5, size * maze['width'], headerHeight )
    renderScore(surface, 10,size * maze['width'],headerHeight)
    width, height , obstacles, bots, coin, screen = maze.values()
    botPositionList = list(map(lambda bot: bot.location, botList))
    for i in range(height):
        for j in range(width):
            location = [i, j]
            if location in botPositionList:
                botIndex = botPositionList.index(location)
                surface.blit(botList[botIndex].image, (j * size, i * size + headerHeight))
            if location == coin:
                surface.blit(coinImage, (j * size, i * size + headerHeight))
            if location in obstacles:
                surface.blit(obstacleImage, (j * size, i * size + headerHeight))
    pygame.display.flip()

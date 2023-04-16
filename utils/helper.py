import json
import time
import pygame


def getJsonData(pathFile):
    try:
        file = open(pathFile, 'r')
        data = json.loads(file.read())
        file.close()
        return data
    except json.decoder.JSONDecodeError:
        time.sleep(0.1)
        return getJsonData(pathFile)


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
    # # surface.blit(time_text, text_rect)
    color = (255, 255, 255)
    pygame.draw.rect(surface, color, pygame.Rect(
        headerWidth // 2.35, (headerHeight//2) - 60 // 2, 120, 60),  0,  3)


def renderScore(surface, botIndex, bot):
    botName = bot.name
    botScore = bot.score
    botImage = bot.image

    color = (255, 255, 255)
    y = 20
    if botIndex % 2 == 0:
        position = "left"
        x = 10
        botX = x
        textX = x + 40
    else:
        position = "right"
        x = 550
        botX = x + 240 - 40
        textX = botX - 40 - 20
    if position == "left":
        pygame.draw.rect(surface, color, pygame.Rect(
            x, y, 240, 60), 0, border_bottom_right_radius=60)

    elif position == "right":
        pygame.draw.rect(surface, color, pygame.Rect(
            x, y, 240, 60), 0, border_bottom_left_radius=60)
        botImage = pygame.transform.flip(botImage, True, False)  # đối xứng ảnh
    surface.blit(botImage, (botX, y + 10))
    renderText(surface, "Score:" + str(botScore), textX, y + 30, 20)
    renderText(surface, "Name:" + str(botName), textX - 10, y + 10, 24)

    pygame.display.flip()


def renderText(surface, text, textX, textY, text_size, center = False):
    font = pygame.font.SysFont('freesansbold.ttf', text_size)
    text = font.render(text, True, 'black')
    if not center:
        surface.blit(text, (textX, textY))
    else:
        text_rect = text.get_rect(center=(textX, textY))
        surface.blit(text, text_rect)


def drawMaze(surface, maze, config, botList, elapsedTime=None):
    headerHeight, size, background, coinImage, obstacleImage = config.values()
    surface.fill((194, 134, 74))
    surface.blit(background, (0, 0 + headerHeight))
    renderTime(surface, elapsedTime, size * maze['width'], headerHeight)
    width, height, obstacles, bots, coin, screen = maze.values()
    # botPositionList = list(map(lambda bot: bot.location, botList))
    for i in range(height):
        for j in range(width):
            location = [i, j]
            for bot in botList:
                if location == bot.location:
                    botIndex = botList.index(bot)
                    renderScore(surface, botIndex, bot)
                    if bot.status != "eliminated":
                        surface.blit(bot.image,
                                        (j * size, i * size + headerHeight))
                    else:
                        surface.blit(bot.eliminated,
                                        (j * size, i * size + headerHeight))
            if location == coin:
                surface.blit(coinImage, (j * size, i * size + headerHeight))
            if location in obstacles:
                surface.blit(obstacleImage, (j * size,
                             i * size + headerHeight))

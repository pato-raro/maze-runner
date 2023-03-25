import pygame as pg 
from pygame.locals import *
pg.init()
import random 
import json
screen_x,screen_y = 30,30
screen_magic_x , screen_magic_y = 0,0
SIZE = 40
# đọc file json băng json :>>
file_open = open('package.json','r')
maze = json.loads(file_open.read())
file_open.close()
WIDTH,HEITH,OBSTACLES,BOT,COIN = maze.values()

def draw():
    screen.fill((0,0,0))
    for i in range(screen_x):
        for j in range(screen_y):
            if [i,j] == BOT:
                screen.blit(boss_display,(j*SIZE,i*SIZE))
            if [i,j] == COIN:
                screen.blit(coin_display,(j*SIZE,i*SIZE))
            if [i,j] in OBSTACLES:
                screen.blit(obstacle_display,(j*SIZE,i*SIZE))
    if screen_magic_x == HEITH and screen_magic_y == WIDTH:
        screen.blit(obstacle_display,(j*SIZE,i*SIZE))
        
#window game 
screen = pg.display.set_mode((WIDTH * SIZE,HEITH* SIZE))
icon = pg.image.load(r'assets\logo.webp')
pg.display.set_icon(icon)
pg.display.set_caption("Boss Obechar Game")
boss_image = pg.image.load(r'assets\granny.webp')
boss_display = pg.transform.scale(boss_image,(SIZE,SIZE))
coin_image = pg.image.load(r'assets\R.png')
coin_display = pg.transform.scale(coin_image,(SIZE,SIZE))
obstacle_image = pg.image.load(r'assets\bingooooo.png')
obstacle_display = pg.transform.scale(obstacle_image,(SIZE,SIZE))
#Game loop
gameplay = True 
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    draw()
    pg.display.update()

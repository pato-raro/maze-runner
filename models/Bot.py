import pygame as pg
from .Character import Character
from time import sleep

pg.init()


class Bot(Character):
    def __init__(self, name, location, status, score):
        super().__init__()
        self.name = name
        self.location = location
        self.status = status
        self.score = score
        self.moveSet = []

    def setMoves(self, dataset):
        file = open(dataset, 'r')
        data = file.readlines()
        data = list(map(lambda step: step.strip(), data))
        self.moveSet = data

    def move(self, direction, time, callback):
        delay = time
        sleep(delay)
        if direction == "up":
            self.location[0] -= 1

        elif direction == "down":
            self.location[0] += 1

        elif direction == "left":
            self.location[1] -= 1

        elif direction == "right":
            self.location[1] += 1
        callback()

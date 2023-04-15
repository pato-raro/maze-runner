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
        self.isOver = False

    def setMoves(self, dataset):
        file = open(dataset, 'r')
        data = file.readlines()
        data = list(map(lambda step: {"direction": step.strip().split(
            " ")[0], "time": step.strip().split(" ")[1]}, data))
        self.moveSet = data

    def gameOver(self):
        if not self.isOver:
            return
            
        self.playSound("death")
        audioDuration = self.deathVoice.get_length() if self.deathVoice != None else 0

        sleep(audioDuration)
        self.status = "eliminated"
        self.moveSet = []

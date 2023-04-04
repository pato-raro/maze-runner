from .Character import Character
import pygame as pg
pg.init()

class Bot(Character): 
    def __init__(self,name, location , status , score ):
        self.name = name
        self.location = location
        self.status = status
        self.score = score
        super().__init__()


    def move(self,direction):
        if direction == "up":
            self.location[0]-=1
           
        elif direction == "down":
            self.location[0]+=1
        
        elif direction == "left":
            self.location[1]-=1
           
        elif direction == "right":
            self.location[1]+=1
        


from utils.helper import getImage
from utils.constants import SCALE_RATIO
import pygame


class Character:
    def __init__(self):
        self.image = None
        self.eliminated = None
        self.killVoice = None
        self.deathVoice = None

    def setImage(self, image):
        self.image = getImage(image, SCALE_RATIO)  # set image

    def setEliminatedImage(self, image):
        self.eliminated = getImage(image, SCALE_RATIO)  # set image

    def setVoices(self, killVoice, deathVoice):  # set voice cho game
        self.killVoice = pygame.mixer.Sound(killVoice)
        self.deathVoice = pygame.mixer.Sound(deathVoice)

    def getAudioLength(self, type):
        if self.killVoice == None or self.deathVoice == None:
            return 0
        if (type == "kill"):
            return self.killVoice.get_length()
        elif (type == "death"):
            return self.deathVoice.get_length()
        else:
            return 0

    def playSound(self, type):
        volume = 0.2
        if self.killVoice == None or self.deathVoice == None:
            return

        if type == "kill":
            pygame.mixer.Channel(0).play(self.killVoice)
            self.killVoice.set_volume(volume)

        elif type == "death":
            pygame.mixer.Channel(1).play(self.deathVoice)
            self.deathVoice.set_volume(volume)
            

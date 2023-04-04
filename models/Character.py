from utils.helper import getImage ,getVoice
from utils.constants import SCALE_RATIO


class Character:
    def __init__(self):
        self.image = None
        self.killVoice = None
        self.deathVoice = None


    def setImage(self , image ):
        self.image  = getImage( image , SCALE_RATIO ) ## set image 


    def setVoices(self , killVoice ,deathVoice ) :  # set voice cho game
        self.killVoice = getVoice( killVoice )
        self.deathVoice = getVoice( deathVoice )
    
    def playSound(self, type):
        if self.killVoice == None or self.deathVoice == None:
            return

        if type == "kill":
            self.killVoice.music.play()

        elif type == "death": 
            self.deathVoice.music.play()
        # if type == "moveBot":
        #     self.moveVoice.music.play()


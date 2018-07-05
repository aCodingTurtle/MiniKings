###############################
#    Screens for MiniKings    #
#        game module 2        #
###############################

from KingsModules import *

class playButton(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(brown)
        self.image.set_colorkey(gold)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        

def menuSetup():
#setup and run menu
    
    window.fill(sand)
    miniTitle = titleFont.render("mini", True, brBlue)
    kingsTitle = titleFont.render("Kings", True, gold)
    window.blit(miniTitle, (200, 100))
    window.blit(kingsTitle, (260, 100))
    pygame.display.update()

"""

def gameStart():
#setup board

def gameScreen():
#get ready for playing

def fightStart():
#setup fighting

def fightScreen():
#get ready for fighting

"""

###############################
#    Imports for MiniKings    #
#        game module 3        #
###############################

# NOTE
# This module inits pygame and creates the game window

import time
import random
import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
titleFont = pygame.font.SysFont("Gentium Basic", 32)

sand = (244,164,96)
brown = (100,65,23)
gold = (255,223,0)
brBlue = (117,244,244)
brGreen = (95,229,6)

import ActionsList as actl
import GameScreens as gs

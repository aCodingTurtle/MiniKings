
 ###############################################################
 #                                                             #
 #                        MiniKings v0.1                       #
 #                                                             #
 ###############################################################


from KingsModules import *

running = True
clock = pygame.time.Clock()
fps = 60

gs.menuSetup()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  gs.startButton = gs.playButton(brown, 150, 200)
  gs.startButton.draw(window)

  clock.tick(FPS)


"""
#interaction functions
def scout(space):
	#stuff

def war(space):
	#stuff - different from fighting

def dHappenings():
	#stuff

def fHappenings():
	#stuff

def manageGov():
	#stuff

"""
#################################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#################################################################

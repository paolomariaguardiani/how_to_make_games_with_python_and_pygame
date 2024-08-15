import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Surface
# - A surface si basically an image!
# - The "display" is also a surface!
# - Meaning that you can draw on any surface!
mySurface = pygame.Surface([840, 480], pygame.SRCALPHA) # we add an alpha channel



myRect = pygame.Rect(200,200, 100, 100)

clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(60) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN: # KEYUP
            if event.key == pygame.K_ESCAPE:
                gameloop = False

    display.fill([25, 25, 25])

    pygame.draw.rect(display, [255, 0, 255], myRect) # filled
    # It is handfull when doing animating sprites and font rendering
    # 
    mySurface.fill([255, 0, 0, 100])
    
    pygame.draw.rect(mySurface, [0,255,0], (250, 250, 100, 100))

    # display.blit(mySurface, [0, 0]) # we put an image on top of another image
    display.blit(mySurface, [0, 0], None, pygame.BLEND_RGBA_ADD) 


    pygame.display.update()



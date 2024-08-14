import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

                    # x, y, widht, height
myRect = pygame.Rect(200,200, 200, 100)

clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(60) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    display.fill([25, 25, 25])

    # Draw stuffs are to be put after the display.fill()

    # myRect.y += 1
    myRect.width += 1 # also myRect.w += 1 is correct
    myRect.h -= 1 # also correct myRect.height
    if myRect.h <= 0:
        myRect.h = 100

        

    pygame.draw.rect(display, [255,255,255], myRect)

    



    pygame.display.update()



import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(5) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    display.fill([random.randint(0, 255), 
                  random.randint(0,255), random.randint(0, 255)])
    



    pygame.display.update()



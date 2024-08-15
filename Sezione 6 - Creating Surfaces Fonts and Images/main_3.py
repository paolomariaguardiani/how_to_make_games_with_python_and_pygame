import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# An image in PyGame is a surface
# Load Image
image = pygame.image.load("data/char1.png")


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
    
    # The third optional parameter is a rectangle.
    # If i get the original size of the image that image won't be changed insize
    display.blit(image, [0, 0])
    

    pygame.display.update()



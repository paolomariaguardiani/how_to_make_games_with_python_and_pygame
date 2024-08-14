import pygame
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

gameloop = True
while gameloop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    display.fill([255, 25, 25])

    pygame.display.update()



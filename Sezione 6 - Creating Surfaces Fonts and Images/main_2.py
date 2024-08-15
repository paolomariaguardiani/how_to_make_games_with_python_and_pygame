import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Font:
# font = pygame.font.Font(fileName, size)
font = pygame.font.SysFont("Arial", 42)
font.set_bold(True)


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
    
    # il quarto parametro opzionale è il backdround color
    text = font.render("Hello, world! Score: " + str(12345), True, [255, 255, 255]) 
    display.blit(text, [10, 10])

    text2 = font.render("New Text!", True, [0, 255, 255]) 
    display.blit(text2, [10, 100])

    pygame.display.update()



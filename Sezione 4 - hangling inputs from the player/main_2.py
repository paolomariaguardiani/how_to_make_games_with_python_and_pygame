import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

                    # x, y, widht, height
myRect = pygame.Rect(200,200, 100, 100)
speed = 10

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
    
        """
        # First approach
        elif event.type == pygame.MOUSEBUTTONDOWN: # or MOUSEBUTTONUP
            if event.button == pygame.BUTTON_LEFT:
                myRect.x -= speed
            elif event.button == pygame.BUTTON_RIGHT:
                myRect.x += speed
        """
    
    mouse = pygame.mouse.get_pressed()

    # mouse is now a tuple wich for left, middle, right buttons of the mouse
    # (False, True, False) it means that the midle button has been pressed
    # pygame.BUTTON_LEFT is 1, pygame.BUTTON_MIDDLE is 2, pygame.BUTTON_RIGHT is 3
    if mouse[pygame.BUTTON_LEFT - 1]: # -1 because pygame.BUTTON_LEFT is 1, but in the tuple is 0 position
        myRect.x -= speed
    elif mouse[pygame.BUTTON_RIGHT -1]: # elif mouse[2] is also correct
        myRect.x += speed
    print(mouse)
    print(pygame.BUTTON_LEFT, pygame.BUTTON_MIDDLE, pygame.BUTTON_RIGHT)

    display.fill([25, 25, 25])

    pygame.draw.rect(display, [255,255,255], myRect) # filled



    pygame.display.update()



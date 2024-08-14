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
            # I checks when the user pressed a key down or a key up
            # Since the player can't go up and down simultaneously we use if - elif statements
            if event.key == pygame.K_w:
                myRect.y -= speed
            elif event.key == pygame.K_s:
                myRect.y += speed

            if event.key == pygame.K_a:
                myRect.x -= speed
            elif event.key == pygame.K_d:
                myRect.x += speed
            """

    # Second approach (it catches the pressed keys)
    # It check if the user is holding a key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        myRect.y -= speed
    elif keys[pygame.K_s]:
        myRect.y += speed
    if keys[pygame.K_a]:
        myRect.x -= speed
    elif keys[pygame.K_d]:
        myRect.x += speed

    
    display.fill([25, 25, 25])

    pygame.draw.rect(display, [255,255,255], myRect) # filled



    pygame.display.update()



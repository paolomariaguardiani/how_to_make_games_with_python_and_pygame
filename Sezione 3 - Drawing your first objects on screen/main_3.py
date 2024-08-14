import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

                    # x, y, widht, height
myRect = pygame.Rect(200,200, 200, 100)

# draw the center of the rectangle at x = 300, y = 300
myRect.center = [300, 300] 

clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(60) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    display.fill([25, 25, 25])

    # Move the rectangle
    # myRect.x += 1

    # Rectangles have a move functions, but they have to be copied
    # copyRect = myRect.move(1, 1) # myRect.move(x, y)
    myRect.move_ip(1, 1) # ip stands for in place
    if myRect.bottom >= display.get_height(): # se raggiungo la parte bassa dello schermo
        myRect.center = (random.randint(0, 300), random.randint(0, 300))

    pygame.draw.rect(display, [255,255,255], myRect)

    



    pygame.display.update()



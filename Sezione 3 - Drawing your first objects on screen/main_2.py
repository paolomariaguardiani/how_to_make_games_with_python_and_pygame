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
# myRect.center = [300, 300] 
# draw the center of the ractangle at the center of the display
myRect.center = [display.get_width() // 2, display.get_height() // 2] 

clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(60) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    display.fill([25, 25, 25])

    # Draw stuffs are to be put after the display.fill()
    # myRect.center = [display.get_width() // 2, display.get_height() // 2] 
    myRect.x += 1        
    # print(myRect.right)
    if myRect.right >= display.get_width():
        myRect.center = (100, 100)

    pygame.draw.rect(display, [255,255,255], myRect)

    



    pygame.display.update()



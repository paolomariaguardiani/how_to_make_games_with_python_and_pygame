import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

                    # x, y, widht, height
myRect = pygame.Rect(200,200, 200, 100)
myRect2 = pygame.Rect(90, 90, 200, 100)
myRect3 = pygame.Rect(650, 200, 170, 90)
myRect4 = pygame.Rect(650, 350, 170, 90)



clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(60) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
    
    display.fill([25, 25, 25])

    pygame.draw.rect(display, [255,255,255], myRect) # filled
    pygame.draw.rect(display, [0, 255, 255], myRect2, 7) # not filled


                    # surface, color, center, radius
    # pygame.draw.circle(display, [255, 0, 0], [300,300], 50)
    pygame.draw.circle(display, [255, 0, 0], myRect.center, 50) # filled
    myRect.move_ip(1, -1)
    
    # the last parameter is the radius of the border of the circle
    pygame.draw.circle(display, [255, 0, 0], [400,400], 50, 4) # not filled
    
    # ellipse needs a rectangle to be drawn on the screen
    pygame.draw.ellipse(display, [255, 0, 255], myRect3) # filled
    pygame.draw.ellipse(display, [0, 255, 255], myRect4, 10) # not filled

    # circle drawn with border and filled (we need two circles)
    pygame.draw.circle(display, (255, 0, 0), (700, 100), 70)
    pygame.draw.circle(display, (0, 255, 0), (700, 100), 70, 10)

    # Draw a line
    pygame.draw.line(display, (255,0,0), (0,0), (myRect.center))
    
    pygame.draw.line(display, (0, 0,255), (30, 30), (840, 30), 7)

    # Draw a poligon
    pygame.draw.polygon(display, (255, 255, 0), [(0,0), (100, 50), (120, 220), (87, 400)], 10)

    pygame.display.update()



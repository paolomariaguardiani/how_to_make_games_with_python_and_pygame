import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Sprite:
# A sprite has an image attached to it and also a rectangle
mySprite = pygame.sprite.Sprite()
mySprite.image = pygame.image.load("data/char1.png")
mySprite.rect = pygame.Rect(200, 200, 100, 100)
# ripristiniamo la grandezza originale dell'immagine
mySprite.image = pygame.transform.scale(mySprite.image, mySprite.rect.size)

# The code below is to get the exact size of the original image // 2
# mySprite.rect = pygame.Rect(200, 200, mySprite.image.get_width() // 2, mySprite.image.get_height() // 2)


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

    mySprite.rect.move_ip(1, -1)
    display.blit(mySprite.image, mySprite.rect)
    

    pygame.display.update()



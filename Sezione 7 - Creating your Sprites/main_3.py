import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Group:
# A sprite group is a "place" to store all those objects (the sprites)
# visibleGroup = pygame.sprite.Group()
# Many differet groups:
# - pygame.sprite.OrderedUpdates() # Renders the sprite in order of addition
visibleGroup = pygame.sprite.OrderedUpdates()



# Sprites:
mySprite = pygame.sprite.Sprite(visibleGroup)
mySprite.image = pygame.image.load("data/char1.png")
mySprite.rect = pygame.Rect(200, 200, 100, 100)
mySprite.image = pygame.transform.scale(mySprite.image, mySprite.rect.size)

otherSprite = pygame.sprite.Sprite(visibleGroup)
otherSprite.image = pygame.image.load("data/char1.png")
otherSprite.rect = pygame.Rect(400, 200, 100, 100)
otherSprite.image = pygame.transform.scale(otherSprite.image, otherSprite.rect.size)

# visibleGroup.add(otherSprite)

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

    mySprite.rect.x += 1
    otherSprite.rect.move_ip(-1, 0)
    # display.blit(mySprite.image, mySprite.rect)
    # display.blit(otherSprite.image, otherSprite.rect)
    visibleGroup.draw(display)

    pygame.display.update()



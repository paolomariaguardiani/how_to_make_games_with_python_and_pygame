import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Group:
visibleGroup = pygame.sprite.Group()

class Character(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("data/char1.png")
        self.rect = pygame.Rect(200,200,100,100)
        self.image = pygame.transform.scale(self.image, self.rect.size)

# Sprite:
char1 = Character(visibleGroup)
char1.rect.center = [150, 150]

char2 = Character(visibleGroup)
char2.rect.center = [350,350]


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

    char1.rect.x += 1
    char2.rect.move_ip(-1, 0)
    # display.blit(mySprite.image, mySprite.rect)
    # display.blit(otherSprite.image, otherSprite.rect)
    visibleGroup.draw(display)

    pygame.display.update()



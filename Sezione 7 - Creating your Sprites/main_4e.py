import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Group:
logicGroup = pygame.sprite.Group()
visibleGroup = pygame.sprite.Group()

class Character(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("data/char1.png")
        self.rect = pygame.Rect(200,200,100,100)
        self.image = pygame.transform.scale(self.image, self.rect.size)

        self.speed = 1

    # We override the update method:
    def update(self):
        self.rect.x += self.speed

        if self.rect.x > 400:
            self.kill()   
            # self.remove(visibleGroup)

# Sprite:
Character(visibleGroup, logicGroup)

char1 = Character(visibleGroup, logicGroup)
char1.rect.center = [150, 150]

char2 = Character(visibleGroup, logicGroup)
char2.rect.center = [350,350]
char2.speed = 3

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

    logicGroup.update()
    visibleGroup.update()

    visibleGroup.draw(display)

    pygame.display.update()



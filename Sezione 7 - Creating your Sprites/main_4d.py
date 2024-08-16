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

        self.speed = 1

    # We override the update method:
    def update(self):
        self.rect.center = [random.randint(0, 300), random.randint(0, 300)]
        self.rect.x += self.speed
        self.rect.y -= self.speed
    

# Sprites:
for i in range(10):
    char1 = Character(visibleGroup)
    
clock = pygame.time.Clock()
gameloop = True

while gameloop:
    clock.tick(10) # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN: # KEYUP
            if event.key == pygame.K_ESCAPE:
                gameloop = False

    display.fill([25, 25, 25])

    # char1.update()
    # char2.update()
    # Use group instead:
    visibleGroup.update()

    visibleGroup.draw(display)

    pygame.display.update()



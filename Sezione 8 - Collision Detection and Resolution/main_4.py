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

keysGroup = pygame.sprite.Group()
charGroup = pygame.sprite.Group()

class Character(pygame.sprite.Sprite):
    # *group perché lo sprite può appartenere a più gruppi contemporaneamente
    def __init__(self, *group): # 
        super().__init__(*group)
        self.image = pygame.image.load("data/char1.png")
        self.rect = pygame.Rect(200,200,100,100)
        self.image = pygame.transform.scale(self.image, self.rect.size)

        self.speed = 1

    # We override the update method:
    def update(self):
        self.rect.x += self.speed


class Key(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load("data/key.png")
        self.rect = pygame.Rect(0, 0, 100, 100)
        # self.rect.center = [random.randint(10, 800), random.randint(10, 400)]
        self.image = pygame.transform.scale(self.image, self.rect.size)


# Sprite:
key1 = Key(visibleGroup, keysGroup)
key1.rect.center = [340,150]

key2 = Key(visibleGroup, keysGroup)
key2.rect.center = [540,150]

char1 = Character(visibleGroup, logicGroup, charGroup)
char1.rect.center = [150, 150]
char1.speed = 2

char2 = Character(visibleGroup, logicGroup, charGroup)
char2.rect.center = [50,350]
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

    ####
    # Third approach:
    # We check the collisions for two groups
    # First boolean: if a character touches a key, do you want to delete the characters?
    # Second boolean: if a key is touched by a character do you want to delete it?
    # This time collisions is a dictionary that map a character to one or more keys 
    #   that it collided with
    collisions = pygame.sprite.groupcollide(charGroup, keysGroup, False, True)
    if collisions: 
        key3 = Key(visibleGroup, keysGroup)
        key3.rect.center = [random.randint(10, 800), random.randint(20, 400)]

    ####

    display.fill([25, 25, 25])

    logicGroup.update()
    visibleGroup.update()

    visibleGroup.draw(display)

    pygame.display.update()



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
    # *group perché lo sprite può appartenere a più gruppi contemporaneamente
    def __init__(self, *group): # 
        super().__init__(*group)
        self.rect = pygame.Rect(200,200,100,100)

        # We specify how many cells the spritesheet has
        self.cells = [9, 5] # 9 columns and 5 rows        
        self.spritesheet = pygame.image.load("data/charTileset.png")
        self.spritesheet = pygame.transform.scale(
            self.spritesheet,
            [self.rect.width * self.cells[0], self.rect.height * self.cells[1]]
        )
        print(self.rect.width)

        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.counter = 36
        self.setTile(1, 1)

    def setTile(self, x, y):
        self.image.fill([0, 0, 0, 0])
        # The value must be negative!!!
        self.image.blit(self.spritesheet, [-self.rect.w * x, -self.rect.h * y])

    # We override the update method:
    def update(self):
        self.counter += 0.2 # this control the speed

        if self.counter > 43:
            self.counter = 36

        c = int(self.counter) # c = int(self.counter / 10) # adjust the value to increase the speed or decrease it
        x = c % self.cells[0]
        y = int(c / self.cells[0]) % self.cells[1]
        self.setTile(x, y)


# Sprites:
char1 = Character(visibleGroup, logicGroup)
char1.rect.center = [150, 150]

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
    logicGroup.update()
      
    display.fill([25, 25, 25])
    visibleGroup.draw(display)

    pygame.display.update()



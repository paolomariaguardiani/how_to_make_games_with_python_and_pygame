import pygame
import random
# from pygame.locals import *

pygame.init()

# sidplay will be a surface
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("My first Game!")

# Load the sounds and music after pygame.init()!
# Music
pygame.mixer.music.load("data/music.wav")
pygame.mixer.music.play(-1)  # -1 play the music forever; 1 = play the music one time

# Sound
shoot = pygame.mixer.Sound("data/shoot.wav")
# shoot.play()


                    # x, y, widht, height
myRect = pygame.Rect(200,200, 100, 100)


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
            elif event.key == pygame.K_SPACE:
                shoot.play()
    

    display.fill([25, 25, 25])

    pygame.draw.rect(display, [255,255,255], myRect) # filled



    pygame.display.update()



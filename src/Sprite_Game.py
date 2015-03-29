import pygame
from pygame.locals import *
import sys
import time
from Sprite import Sprite 

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255, 255, 255))
sprite = Sprite(320, 240, screen)
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False


while not done:    
    pygame.event.pump()
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        sprite.move_west()
    if keys[K_RIGHT]:
        sprite.move_east()
    if keys[K_UP]:
        sprite.move_north()
    if keys[K_DOWN]:
        sprite.move_south()
    if keys[K_ESCAPE]:
        done = True
    time.sleep(0.05)
    
    """
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite.move_west()
            if event.key == pygame.K_RIGHT:
                sprite.move_east()
            if event.key == pygame.K_UP:
                sprite.move_north()
            if event.key == pygame.K_DOWN:
                sprite.move_south()
 """




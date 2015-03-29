import pygame
from pygame.locals import *
import sys
import time
from Sprite import Sprite 
import random

pygame.init()

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255, 255, 255))
player_sprite = Sprite(320, 240, screen, (255, 0, 0))
comp_sprite = Sprite(0, 0, screen, (0, 255, 0))
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False

direction = random.randint(0, 3)

while not done:    
    pygame.event.pump()
    keys=pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_sprite.move_west()
    if keys[K_RIGHT]:
        player_sprite.move_east()
    if keys[K_UP]:
        player_sprite.move_north()
    if keys[K_DOWN]:
        player_sprite.move_south()
    if keys[K_ESCAPE]:
        done = True
    decision = random.randint(0, 5)
    print ("decision number is ", decision)
    if 0 == decision:
        direction = random.randint(0, 3)
        print ("new direction is ",  direction)

    if direction == 0:
        comp_sprite.move_north()
    if direction == 1:
        comp_sprite.move_south()
    if direction == 2:
        comp_sprite.move_west()
    if direction == 3:
        comp_sprite.move_east()
    done = player_sprite.is_at_same_coordinates( comp_sprite )
    #for event in pygame.event.get(): # User did something
    time.sleep(0.05)
    
    """
    # --- Main event loop
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_sprite.move_west()
            if event.key == pygame.K_RIGHT:
                player_sprite.move_east()
            if event.key == pygame.K_UP:
                player_sprite.move_north()
            if event.key == pygame.K_DOWN:
                player_sprite.move_south()
 """




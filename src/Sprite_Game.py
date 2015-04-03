import pygame
from pygame.locals import *
import sys
import time
from Sprite import SuperSprite 
import random

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GHOST_COUNT = 1000
score = 0

def render_score( screen ):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score " + str(score), True, WHITE)
    screen.blit(text, [screen.get_width() - 100, 10])
    
pygame.init()
pygame.display.set_caption("Get all 1000 ghosts")
screen = pygame.display.set_mode((1024,800))

pacman = SuperSprite("Pacman",  320, 240, screen,"../images/PacMK1.png")
pacman_group = pygame.sprite.Group()
pacman_group.add(pacman)

ghost_group = pygame.sprite.Group()
for ghosts in range(0, GHOST_COUNT):
    ghost_x = random.randint(0, screen.get_width() -24)
    ghost_y = random.randint(40, screen.get_height() -24)
    ghost = SuperSprite("Ghost " + str(ghosts),  ghost_x, ghost_y, screen, "../images/GhostMK1.png")
    ghost.direction = random.randint(0, 3)
    ghost_group.add(ghost)
    
clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False

direction = random.randint(0, 3)
pygame.display.update()
while not done:    
    
    pygame.event.pump()
    keys=pygame.key.get_pressed()
    pacman.direction = SuperSprite.STATIONARY
    if keys[K_LEFT]:
        pacman.direction = SuperSprite.WEST
        pacman.move()
    if keys[K_RIGHT]:
        pacman.direction = SuperSprite.EAST
        pacman.move()
    if keys[K_UP]:
        pacman.direction = SuperSprite.NORTH
        pacman.move()
    if keys[K_DOWN]:
        pacman.direction = SuperSprite.SOUTH
        pacman.move()
    if keys[K_ESCAPE]:
        done = True
    
    

    for ghost in ghost_group.sprites():
        decision = random.randint(0, 5)
        #print ("decision number is ", decision)
        if 0 == decision:
            ghost.direction = random.randint(0, 3)
            #print ("new direction is ",  ghost.direction)
        ghost.move()
        
    collisions = pygame.sprite.groupcollide(pacman_group,  ghost_group,  False,  True)
    
    if len(collisions) > 0:
        score += len( collisions[pacman] )

            
    # Render everything
    screen.fill(BLUE)
    pacman_group.draw(screen)
    ghost_group.draw(screen)
    render_score(screen)  
    pygame.display.update()  
    
    #for event in pygame.event.get(): # User did something
    time.sleep(0.02)





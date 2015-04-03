import pygame
from pygame.locals import *
import sys
import time
from Sprite import SuperSprite 
import random

BLUE = (0, 0, 255)
RED = (255,  0,  0)
WHITE = (255, 255, 255)
GHOST_COUNT = 80
score = 0
lives = 3

def render_score( screen ):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    score_text = font.render("Score " + str(score), True, WHITE)
    screen.blit(score_text, [screen.get_width() - 100, 10])
    lives_text = font.render("Lives " + str(lives), True, WHITE)
    screen.blit(lives_text, [20, 10])
    
pygame.init()
pygame.display.set_caption("Get all 1000 ghosts")
screen = pygame.display.set_mode((1024,800))

pacman = SuperSprite("Pacman",  320, 240, screen,"../images/PacMK1.png")
pacman_group = pygame.sprite.Group()
pacman_group.add(pacman)

ghost_group = pygame.sprite.Group()
for ghosts in range(0, GHOST_COUNT):
    is_evil = random.randint(0, 20) == 0
    ghost_x = random.randint(0, screen.get_width() -24)
    ghost_y = random.randint(40, screen.get_height() -24)
    ghost = None
    if is_evil:
        ghost = SuperSprite("Evil Ghost",  ghost_x, ghost_y, screen, "../images/EvilGhost.png")
    else:
        ghost = SuperSprite("Ghost",  ghost_x, ghost_y, screen, "../images/GhostMK1.png")
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
    background_colour = BLUE
    if len(collisions) > 0:
        for collided_ghost in collisions[pacman]:
            if collided_ghost.is_evil():
                background_colour = RED
                lives -= 1
                if lives == 0:
                    done = True
        
        score += len( collisions[pacman] )

            
    # Render everything
    screen.fill(background_colour)
    pacman_group.draw(screen)
    ghost_group.draw(screen)
    render_score(screen)  
    pygame.display.update()  
    
    #for event in pygame.event.get(): # User did something
    time.sleep(0.02)





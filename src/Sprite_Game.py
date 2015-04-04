import pygame
from pygame.locals import *
from Colours import *
import sys
import time
from Sprite import SuperSprite
from Sprite import Wall
import random

difficulty = raw_input ("Enter easy, medium, hard or test ")
lives = 3
GHOST_COUNT = 175
if difficulty.lower() ==  "medium":
    lives = 2
    GHOST_COUNT = 250
if difficulty.lower() == "hard":
    lives = 1
    GHOST_COUNT = 500
if difficulty.lower() == "test":
    lives_string = raw_input("Number of lives: ")
    lives = int(lives_string)
    ghost_count_string = raw_input("Number of ghosts: ")
    GHOST_COUNT  = int(ghost_count_string)


score = 0

def render_score( screen, image_number):
    font = pygame.font.SysFont('Calibri', 25, True, False)
    score_text = font.render("Score " + str(score), True, WHITE)
    screen.blit(score_text, [screen.get_width() - 100, 10])


    score_icon_group = pygame.sprite.Group()
    for life in range(0, lives):
        x = 20 + (life * 29)
        score_icon_group.add(SuperSprite("Score",  x, 10, screen,"../images/open_closed_pac.png",2, image_number, None))
    score_icon_group.draw(screen)


pygame.init()
pygame.display.set_caption("Don't get eaten by zombie ghosts and eat red ghosts as pac man")
screen = pygame.display.set_mode((1024,800))

walls = pygame.sprite.Group()
wall_file = open('../resources/walls.csv', 'r')
for line in wall_file:
        coords = [int(x) for x in line.split(',')]
        walls.add(Wall(coords[0],coords[1],coords[2],coords[3] ))

pacman = SuperSprite("Pacman",  320, 240, screen,"../images/open_closed_pac.png", 2, 0, walls)
pacman_group = pygame.sprite.Group()
pacman_group.add(pacman)

pacman_wasd = SuperSprite("Pacman",  360, 240, screen,"../images/open_closed_pac_wasd.png", 2, 0, walls)
pac_wasd_group = pygame.sprite.Group()
pac_wasd_group.add(pacman_wasd)

ghost_group = pygame.sprite.Group()
evil_ghost_count = GHOST_COUNT / 20
if evil_ghost_count < lives:
    evil_ghost_count = lives
for ghosts in range(0, GHOST_COUNT):
    ghost_x = random.randint(0, screen.get_width() -24)
    ghost_y = random.randint(40, screen.get_height() -24)
    ghost = None
    if ghosts < evil_ghost_count:
        ghost = SuperSprite("Evil Ghost",  ghost_x, ghost_y, screen, "../images/EvilGhost.png",  1, 0, walls)
    else:
        ghost = SuperSprite("Ghost",  ghost_x, ghost_y, screen, "../images/GhostMK1.png",  1, 0, walls)
    ghost.direction = random.randint(0, 3)
    ghost_group.add(ghost)

clock = pygame.time.Clock()
# Loop until the user clicks the close button.
done = False

direction = random.randint(0, 3)
pygame.display.update()
frame_count = 0
pacman_image = 0
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
        score += len( collisions[pacman] )
        for collided_ghost in collisions[pacman]:
            if collided_ghost.is_evil():
                background_colour = RED
                lives -= 1
                GHOST_COUNT -= 1
                if lives == 0:
                    done = True

        #self.image.fill(BLUE)
        #open_group.draw(screen)

    frame_count += 1
    if frame_count % 10 == 0:
        pacman_image = 1 if pacman_image == 0 else 0
        pacman.select_image(pacman_image)

    # Render everything
    screen.fill(background_colour)
    pacman_group.draw(screen)
    pac_wasd_group.draw(screen)
    ghost_group.draw(screen)
    walls.draw(screen)
    render_score(screen, pacman_image)
    pygame.display.update()


    #for event in pygame.event.get(): # User did something
    time.sleep(0.015)





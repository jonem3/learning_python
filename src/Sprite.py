import pygame
from pygame.sprite import Sprite
import random
from Colours import *
import time


class SuperSprite(Sprite):
   
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    STATIONARY = -1
    
    SPRITE_DIMENSION = 24
    
    STANDARD_STEP = 5
    EVIL_STEP = random.randint(3, 12)

    def __init__(self,  name,  x,  y,  screen,  image,  image_count,  walls):
        # Call the parent class (Sprite) constructor
        super(SuperSprite, self).__init__()
        # Load the image
        self.sprite_sheet = pygame.image.load(image).convert()
        # Create a new blank image
        self.image = pygame.Surface([SuperSprite.SPRITE_DIMENSION, SuperSprite.SPRITE_DIMENSION]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        self.image.blit(self.sprite_sheet, (0, 0), (0, 0, SuperSprite.SPRITE_DIMENSION, SuperSprite.SPRITE_DIMENSION))
        
        self.image_count = image_count
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.screen = screen
        self.walls = walls
        self.direction = SuperSprite.STATIONARY
        
    def select_image(self,  image_number):
        if image_number < 0 or image_number > self.image_count:
            print "coding error, image number out of scope"
            exit(1)
        sprite_sheet_x = image_number * 24
        self.image.blit(self.sprite_sheet, (0, 0), (sprite_sheet_x, 0, SuperSprite.SPRITE_DIMENSION, SuperSprite.SPRITE_DIMENSION))
    
    def move(self):
        step = random.randint(3, 15) if self.is_evil() else SuperSprite.STANDARD_STEP
        old_x = self.rect.x
        old_y = self.rect.y
        if self.direction == SuperSprite.NORTH and self.rect.y > 40:
            self.rect.y -= step                     
        if self.direction == SuperSprite.SOUTH and self.rect.y < self.screen.get_height() - self.rect.height:
            self.rect.y += step
        if self.direction == SuperSprite.WEST and self.rect.x > 0:
            self.rect.x -= step
        if self.direction == SuperSprite.EAST and self.rect.x < self.screen.get_width() - self.rect.width:
            self.rect.x += step  
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        if len(block_hit_list) > 0:
            self.rect.y = old_y
            self.rect.x = old_x
            
    def is_evil(self):
        return self.name.startswith("Evil")
            
    def __repr__(self):
        return self.name + ' at ' + str(self.rect.x) + ',' + str(self.rect.y)


class Wall(Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super(Wall,  self).__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

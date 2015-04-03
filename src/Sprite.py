import pygame
from pygame.sprite import Sprite
class SuperSprite(Sprite):
   
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    STATIONARY = -1
    
    step = 5

    def __init__(self,  name,  x,  y,  screen,  image):
        # Call the parent class (Sprite) constructor
        super(SuperSprite, self).__init__()
        # Load the image
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.screen = screen
        self.direction = SuperSprite.STATIONARY
        
    def move(self):
        if self.direction == SuperSprite.NORTH and self.rect.y > 40:
            self.rect.y -= SuperSprite.step
        if self.direction == SuperSprite.SOUTH and self.rect.y < self.screen.get_height() - self.rect.height:
            self.rect.y += SuperSprite.step
        if self.direction == SuperSprite.WEST and self.rect.x > 0:
            self.rect.x -= SuperSprite.step
        if self.direction == SuperSprite.EAST and self.rect.x < self.screen.get_width() - self.rect.width:
            self.rect.x += SuperSprite.step  
            
    def __repr__(self):
        return self.name + ' at ' + str(self.rect.x) + ',' + str(self.rect.y)


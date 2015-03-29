import pygame

class Sprite:
   
    step = 5
   
    def __init__(self,  x,  y,  screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.draw_sprite()
        
    def move_north(self):
        self.rm_sprite()
        self.y -= Sprite.step
        self.draw_sprite()
        
    def move_south(self):
        self.rm_sprite()
        self.y += Sprite.step
        self.draw_sprite()
        
    def move_east(self):
        self.rm_sprite()
        self.x += Sprite.step
        self.draw_sprite()
        
    def move_west(self):
        self.rm_sprite()
        self.x -= Sprite.step
        self.draw_sprite()
        
    def rm_sprite(self):
        pygame.draw.circle(self.screen,  (255, 255, 255), (self.x, self.y), 10, 2)
        
    def draw_sprite(self):
        pygame.draw.circle(self.screen,  (255, 0, 0), (self.x, self.y), 10, 2)
        pygame.display.update()

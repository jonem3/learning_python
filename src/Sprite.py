import pygame

class Sprite:
   
    step = 5
    radius = 5
    def __init__(self,  x,  y,  screen,  colour):
        self.x = x
        self.y = y
        self.screen = screen
        self.colour = colour
        self.draw_sprite()
        
    def move_north(self):
        if self.y > self.radius:
            self.rm_sprite()
            self.y -= Sprite.step
            self.draw_sprite()
        
    def move_south(self):
        if self.y <  self.screen.get_height() - self.radius:
            self.rm_sprite()
            self.y += Sprite.step
            self.draw_sprite()
        
    def move_east(self):
        if self.x < self.screen.get_width() - self.radius:
            self.rm_sprite()
            self.x += Sprite.step
            self.draw_sprite()
        
    def move_west(self):
        if self.x > self.radius:
            self.rm_sprite()
            self.x -= Sprite.step
            self.draw_sprite()
        
    def rm_sprite(self):
        pygame.draw.circle(self.screen,  (0, 0, 255), (self.x, self.y), self.radius*2, 2)
    def draw_sprite(self):
        pygame.draw.circle(self.screen,  self.colour, (self.x, self.y), self.radius*2, 2)
        pygame.display.update()
        
    def is_at_same_coordinates(self,  other_sprite):
        return self.x == other_sprite.x and self.y == other_sprite.y

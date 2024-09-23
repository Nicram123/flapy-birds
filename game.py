import pygame 
from constants import screen_width, screen_height, hole_size, spacing_between_obstacles, increase, fly_cord_up, fly_cord_down
import random 

class Bird:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.pic = pygame.image.load('bird.png')
    self.pic = pygame.transform.scale(self.pic, (int(self.pic.get_width() * increase), int(self.pic.get_height() * increase)))
  
  def create_obstacles(self):
    x = random.randint(0, screen_height)
    
  def generate_bird(self, screen):
    screen.blit(self.pic, (self.x, self.y))
    
  def increase_bird(self):
    self.y -= fly_cord_up
  
  def fall_bird(self):
    self.y += fly_cord_down
    
  

    
    
    



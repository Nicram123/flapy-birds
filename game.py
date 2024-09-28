import pygame 
from constants import score_pos, white, pic, move_obstacles, bottom, top, screen_width, screen_height, hole_size, spacing_between_obstacles, increase, fly_cord_up, fly_cord_down
import random 
import sys

class Bird:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.obst_cord = []
    self.flag = True
    self.score = 0
    
  def generate_first_two_obstacles(self):
    if len(self.obst_cord) != 2:
      if self.flag == True:
        cor = random.randint(0, screen_height - 10) # > 145 
        cor = self.coordinate(cor)
        self.obst_cord.append([screen_width, cor, True]) 
        self.flag = False
      if screen_width - self.obst_cord[0][0] > spacing_between_obstacles:
         cor = random.randint(0, screen_height - 10) # > 145 
         cor = self.coordinate(cor)
         self.obst_cord.append([screen_width, cor, True]) 
         
  def generate_rest_obstacles(self):
    if len(self.obst_cord) == 2 and self.obst_cord[0][0] < 0: 
      if len(self.obst_cord) == 2: 
        self.obst_cord.pop(0)
      cor = random.randint(0, screen_height - 10) # > 145 
      cor = self.coordinate(cor)
      self.obst_cord.append([screen_width, cor, True])
      self.flag = False
      
  def show_list_of_all_obstacles(self, screen):
    for corX, corY, _ in self.obst_cord:
      screen.blit(bottom, (corX, corY))
      screen.blit(top, (corX, corY - 650))
      
  def create_obstacles(self, screen):
    self.generate_first_two_obstacles()
    self.generate_rest_obstacles()
    self.show_list_of_all_obstacles(screen)
    self.move_obstacles()
      
  def move_obstacles(self):
    for x in range(len(self.obst_cord)):
      self.obst_cord[x][0] -= move_obstacles
      
  def coordinate(self, cor):
    if cor < 150:
      cor += 150 - cor + 1
    return cor 
  
  def draw_score(self, screen, font):
    self.increment_score()
    score_text = font.render(f'{self.score}', True, white)
    screen.blit(score_text, score_pos)
    
        
  def increment_score(self):
    if self.obst_cord[0][2] == True and self.x >= self.obst_cord[0][0]:
      self.score += 1
      self.obst_cord[0][2] = False
    if len(self.obst_cord) ==2 and self.obst_cord[1][2] == True and self.x >= self.obst_cord[1][0]:
      self.score += 1
      self.obst_cord[1][2] = False
  
  def generate_bird(self, screen):
    screen.blit(pic, (self.x, self.y))
    
  def increase_bird(self):
    self.y -= fly_cord_up
  
  def fall_bird(self):
    self.y += fly_cord_down
    
  

    
    
    



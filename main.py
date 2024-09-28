import pygame
import sys
from game import Bird 
from constants import screen_height, screen_width

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

pic = pygame.image.load('background.png')
pic = pygame.transform.scale(pic, (screen_width, screen_height))

font = pygame.font.SysFont(None, 48)

bird = Bird(300, 300)
start_flag = False

flag = True



while True:
  
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    start_flag = True
    
  if start_flag == True and keys[pygame.K_SPACE]:  # Ptak wznosi się
        bird.increase_bird()
        
  if start_flag == True and not any(keys):
      bird.fall_bird() 
    
  
  #bird.constrain_position()
  #bird.increase_bird()
        
      
    
  screen.blit(pic, (0, 0))
  
  
  bird.generate_bird(screen)
  bird.create_obstacles(screen)
  bird.draw_score(screen, font)
  #flag = False
  
  
  pygame.display.update()


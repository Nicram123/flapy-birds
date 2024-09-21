import pygame
import sys 
from constants import screen_height, screen_width

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

pic = pygame.image.load('background.png')
pic = pygame.transform.scale(pic, (screen_width, screen_height))



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.blit(pic, (0, 0))
  pygame.display.update()


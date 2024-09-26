import pygame

screen_width, screen_height = 500, 500
hole_size = 50
spacing_between_obstacles = 250
increase = 1.7
fly_cord_up = 0.5
fly_cord_down = 0.2

bottom = pygame.image.load('pipebottom.png')
top = pygame.image.load('pipetop.png')

pic = pygame.image.load('bird.png')
pic = pygame.transform.scale(pic, (int(pic.get_width() * increase), int(pic.get_height() * increase)))

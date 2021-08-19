import pygame
from rocket import *
#screen info
background_colour = (150,150,150)
(width, height) = (600,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
screen.fill(background_colour)
pygame.display.flip()
running = True
#rocket info
rocket_dim_x = 30
rocket_dim_y = 250
r = Rocket(rocket_dim_x,rocket_dim_y,width/2-rocket_dim_x/2,height/2-rocket_dim_y/2,screen,(255,255,255))

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  r.draw()
  py.display.update()

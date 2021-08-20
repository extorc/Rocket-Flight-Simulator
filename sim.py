import pygame
from rocket import *

#screen info
background_colour = (150,150,150)
(width, height) = (600,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
pygame.display.flip()
running = True
clock = py.time.Clock()
fps = 30
#rocket info
rocket_dim_x = 30
rocket_dim_y = 250
r = Rocket(rocket_dim_x,rocket_dim_y,width/2-rocket_dim_x/2,height/2-rocket_dim_y/2,screen,(255,255,255),fps,90)
while running:
  clock.tick(fps)
  screen.fill(background_colour)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  r.rotation()
  py.display.update()

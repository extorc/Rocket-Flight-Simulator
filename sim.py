import pygame
from rocket import *

background_colour = (150,150,150)
(width, height) = (600,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulator')
screen.fill(background_colour)
pygame.display.flip()
running = True
rocket_dim = 30
r = Rocket(rocket_dim,rocket_dim,width/2-rocket_dim/2,height/2-rocket_dim/2,screen)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  r.draw()
  py.display.update()

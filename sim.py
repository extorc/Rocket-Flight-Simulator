import pygame
from rocket import *

class Sim:
    def __init__(self,bgcolor,dim,caption,fps,rocket_color,rotation):
        self.bgcolor = bgcolor
        self.screen = pygame.display.set_mode(dim)
        pygame.display.set_caption(caption)
        pygame.display.flip()
        self.running = True
        self.clock = py.time.Clock()
        self.fps = fps
        #rocket info
        rocket_dim_x = 30
        rocket_dim_y = 250
        mid_pos = (dim[0]/2-rocket_dim_x/2,dim[1]/2-rocket_dim_y/2)
        self.rocket = Rocket(rocket_dim_x,rocket_dim_y,mid_pos[0],mid_pos[1],self.screen,(255,255,255),self.fps,rotation)
    def simulate(self):
        while self.running:
          self.clock.tick(self.fps)
          self.screen.fill(self.bgcolor)
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.running = False
          self.rocket.rotation()
          py.display.update()

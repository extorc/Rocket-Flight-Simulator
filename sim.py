import pygame
from rocket import *
class Sim:
    def __init__(self,bgcolor,dim,caption,fps,rocket_color,rotation,desired_rot,mmoi):
        self.bgcolor = bgcolor
        self.screen = pygame.display.set_mode(dim)
        pygame.display.set_caption(caption)
        pygame.display.flip()
        self.running = True
        self.clock = py.time.Clock()
        self.fps = fps
        rocket_dim_x = 30
        rocket_dim_y = 250
        self.color = rocket_color
        mid_pos = (dim[0]/2-rocket_dim_x/2,dim[1]/2-rocket_dim_y/2)
        self.rocket = Rocket(rocket_dim_x,rocket_dim_y,mid_pos[0],mid_pos[1],self.screen,self.color,self.fps,rotation,mmoi)
        self.desired_rot = desired_rot
        self.error = desired_rot-self.rocket.angle
        self.error_log = []
    def simulate(self):
        while self.running:
          self.clock.tick(self.fps)
          self.screen.fill(self.bgcolor)
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.running = False
          self.error_log.append(self.get_error())
          p,i,d = self.compute_pid(self.get_error(),self.error_log,1,1,1)
          self.rocket.rotational_speed = p/self.fps
          # print(i,d)
          print(self.rocket.rotational_speed)
          self.rocket.rotation()
          py.display.update()
    def get_error(self):
        return self.desired_rot-self.rocket.angle
    def compute_pid(self,error,error_log,pg,ig,dg):
        pgain = pg
        dgain = dg
        Igain = ig
        Iedx = 0
        i = 0
        p = error * pgain
        try:
            d_error = error_log[len(error_log)-3]
            d_2error = error_log[len(error_log)-1]
        except:
            d_error = 0
            d_2error = 0
        d = dgain*((d_error-d_2error)/3)
        for e in error_log:
            Iedx += e
        i = Iedx
        Iedx = 0
        i = i * Igain
        return (p,i,d)

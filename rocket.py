import pygame as py

class Rocket:
    def __init__(self,x,y,l,t,screen,color,fps,rs):
        self.x = x
        self.y = y
        self.l = l
        self.t = t
        self.sim_fps = fps
        self.surface = py.Surface((self.x,self.y),py.SRCALPHA)
        self.screen = screen
        self.color = color
        self.surface.fill(self.color)
        self.rotated_surface = self.surface
        self.rotational_speed = rs/fps
        self.angle = 0
    def rotation(self):
        self.angle += self.rotational_speed
        self.rotated_surface = py.transform.rotate(self.surface, self.angle)
        self.rect = self.rotated_surface.get_rect(center = (self.l + self.x/2,self.t + self.y/2))
        self.screen.blit(self.rotated_surface, (self.rect.x, self.rect.y))
    def set_angle(self,angle):
        self.angle = angle

import pygame as py

class Rocket:
    def __init__(self,x,y,l,t,screen):
        self.x = x
        self.y = y
        self.l = l
        self.t = t
        self.screen = screen
    def draw(self):
        py.draw.rect(self.screen,(255,255,255),py.Rect(self.l,self.t,self.x,self.y))

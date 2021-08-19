import pygame as py

class Rocket:
    def __init__(self,x,y,l,t,screen,color):
        self.x = x
        self.y = y
        self.l = l
        self.t = t
        self.surface = py.Surface((self.x,self.y))
        # self.rect = py.Rect(self.l,self.t,self.x,self.y)
        self.screen = screen
        self.color = color
    def draw(self):
        self.surface.fill(self.color)
        self.screen.blit(self.surface,(self.l,self.t))
        # py.draw.rect(self.screen,self.color,self.rect)

import pygame
from game import game

pygame.init()
class playerobj(game):
    def __init__(self,x,y,speed,width, height) -> None:
        super().__init__
        self.x = x
        self.width = width 
        self.height = height
        self.y = y
        self.spd = speed
    def render(self):
        rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(self.screen,self.rectcolor, rect)

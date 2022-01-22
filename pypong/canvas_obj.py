import pygame
import math


class CanvasObject:
    def __init__(self) -> None:
        self.width = 20
        self.height = 130
        self.bsize = 25
        self.speed = 3
        self.x, self.y = 300, 450
        self.rectcolor = (255, 255, 255)
        self.upp1 = False
        self.downp1 = False
        self.upp2 = False
        self.downp2 = False
        self.up = False
        self.down = True
        self.right = False
        self.left = True
        self.px1 = 50
        self.py1 = 150
        self.px2 = 850
        self.py2 = 150
        self.HEIGHT, self.WIDTH = 600, 900
    # TODO: check colision
    def collision(self, px,py,x,y):
        distance = math.sqrt(math.pow((x - px), 2) + math.pow((y- py), 2))
        print(distance)
        print(x, y, px, py)
        



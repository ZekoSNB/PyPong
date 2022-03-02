from re import T
import pygame
import math


class CanvasObject:
    def __init__(self) -> None:
        self.width = 20
        self.height = 130
        self.bsize = 25
        self.speed = 5
        self.bspeed = 2.5
        self.bspeedy = 3
        self.x, self.y = 300, 450
        self.rectcolor = (255, 255, 255)
        self.count1 = 0
        self.count2 = 0
        self.upp1 = False
        self.downp1 = False
        self.upp2 = False
        self.downp2 = False
        self.up = False
        self.down = True
        self.right = False
        self.left = True
        self.px1 = 50
        self.py1 = 0
        self.px2 = 850
        self.py2 = 150
        self.HEIGHT, self.WIDTH = 600, 900

    # TODO: check colision
    def collision(self, px, py, x, y, p):
        if px > 450:
            if y >= (py - self.bsize + 10) and y <= (py + self.height + self.bsize - 10) and px == (x + self.bsize / 2):
                return True
        if px < 450:
            if y >= (py - self.bsize + 10) and y <= (py + self.height + self.bsize - 10) and px == (x - self.bsize / 2):
                return True

    def score(self, num1, num2, screen, x, y):
        text = self.scr_font.render(f"Player1: {num1} | Player2: {num2}", True, (255, 255, 255))
        screen.blit(text, (x, y))

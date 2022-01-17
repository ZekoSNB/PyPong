import pygame


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
        self.right = True
        self.left = False
        self.HEIGHT, self.WIDTH = 600, 900
    # TODO: check colision
    def collision(self):
        pass



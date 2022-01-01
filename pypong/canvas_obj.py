import pygame


class CanvasObject:
    def __init__(self) -> None:
        self.width = 20
        self.height = 130
        self.bsize = 25
        self.speed = 3
        self.rectcolor = (255, 255, 255)
        self.upp1 = False
        self.downp1 = False
        self.upp2 = False
        self.downp2 = False
    # TODO: check colision
    def collision(self):
        pass



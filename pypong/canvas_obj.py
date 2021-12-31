import pygame


class CanvasObject:
    def __init__(self) -> None:
        self.width = 10
        self.height = 30
        self.speed = 5
        self.rectcolor = (255, 255, 255)
        self.up = False
        self.down = False
    # TODO: check colision
    def collision(self):
        pass



import pygame


class CanvasObject:
    def __init__(self, speed, width, height, screen) -> None:
        self.width = width
        self.height = height
        self.speed = speed
        self.rectcolor = (255, 255, 255)
        self.screen = screen
        self.up = False
        self.down = False
    # TODO: check colision
    def collision(self):
        pass

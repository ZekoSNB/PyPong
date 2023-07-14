import pygame
import abc
from enum import Flag, auto


class CanvasObject(abc.ABC):
    class Direction(Flag):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    def __init__(self, x, y, width, height, screen) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rectcolor = (255, 255, 255)

    def collision(self, other: 'CanvasObject'):
        if (max(self.x + self.width, other.x + other.width) - min(self.x, other.x)) \
                < (self.width + other.width) and \
                (max(self.y + self.height, other.y + other.height) - min(self.y, other.y)) \
                < (self.height + other.height):
            return True

    def render(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.rectcolor, rect)

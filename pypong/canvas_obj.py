import pygame


class CanvasObject:
    def __init__(self, x, y, speed, width, height, screen) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spd = speed
        self.screen = screen

    def render(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # TODO fix rectcolor
        pygame.draw.rect(self.screen, self.rectcolor, rect)

    # TODO: check colision

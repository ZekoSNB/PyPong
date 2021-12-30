from pypong.canvas_obj import CanvasObject
import pygame


class Player(CanvasObject):
    def __init__(self, x, y,screen) -> None:
        super.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
    def render(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # TODO fix rectcolor
        pygame.draw.rect(self.screen, self.rectcolor, rect)
    def move(self):
        if self.up:
            self.y += self.speed
        if self.down:
            self.y -= self.speed

from pypong.canvas_obj import CanvasObject
import pygame


class Player(CanvasObject):
    def __init__(self, x, y,screen) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
    def render(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.rectcolor, self.rect)

    def move(self,stateup, statedown):
        if stateup:
            self.y -= self.speed
        if statedown:
            self.y += self.speed
        # if self.down and self.up:
            # self.y = self.y

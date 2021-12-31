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
        print(self.up)

    def move(self):
        if self.up:
            self.y += self.speed
            print('Moving up')
        if self.down:
            self.y -= self.speed
        if self.down and self.up:
            self.y = self.y

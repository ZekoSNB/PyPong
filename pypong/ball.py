from pypong.canvas_obj import CanvasObject
import pygame


class Ball(CanvasObject):
    def __init__(self,x,y,screen) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.src = screen
    def render(self):
        self.rect = pygame.Rect(self.x, self.y, self.bsize, self.bsize)
        pygame.draw.rect(self.src, self.rectcolor, self.rect)
    


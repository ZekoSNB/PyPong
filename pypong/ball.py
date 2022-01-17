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
    def border(self):
        if self.y >= (self.HEIGHT - self.bsize):
            return 'up'
        if self.y < 0:
            return 'down'
    def move(self, up,down,left,right):
        if up and right:
            self.x += self.speed
            self.y -= self.speed
        if up and left:
            self.x -= self.speed
            self.y -= self.speed
        if down and left:
            self.x -= self.speed
            self.y += self.speed
        if down and right:
            self.x += self.speed
            self.y += self.speed
    


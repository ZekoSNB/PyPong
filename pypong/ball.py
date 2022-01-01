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
    # TODO: Move a ball
    def border(self, upp, dow, y):
        self.up = upp
        print(self.WIDTH, y)
        self.down = dow
        if y >= (self.WIDTH - self.bsize):
            self.up = True
            self.down = False
        if y <= (0 + 25):
            self.down = True
            self.up = False
    def move(self, up,down,left,right,x,y):
        if up and right:
            x += self.speed
            y -= self.speed
        if up and left:
            x -= self.speed
            y += self.speed
        if down and left:
            x -= self.speed
            y -= self.speed
        if down and right:
            x += self.speed
            y += self.speed
    


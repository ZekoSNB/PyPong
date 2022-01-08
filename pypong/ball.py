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
    def border(self):
        print(self.up,self.down,self.right,self.left)
        if self.y >= (self.WIDTH - self.bsize):
            self.up = True
            self.down = False
        if self.y < (0 + 25):
            print("Working")
            self.down = True
            self.up = False
            return self.down
    def move(self, up,down,left,right):
        if up and right:
            self.x += self.speed
            self.y -= self.speed
        if up and left:
            self.x -= self.speed
            self.y += self.speed
        if down and left:
            self.x -= self.speed
            self.y -= self.speed
        if down and right:
            self.x += self.speed
            self.y += self.speed
    


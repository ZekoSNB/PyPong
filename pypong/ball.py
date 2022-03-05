from pypong.canvas_obj import CanvasObject


class Ball(CanvasObject):
    def __init__(self, x, y, screen) -> None:
        super().__init__(x, y, 25, 25, screen)
        self.bspeed = 2.5
        # self.bspeedy = 3
        self.dir = self.Direction.UP | self.Direction.LEFT

    def move(self):
        if self.dir & self.Direction.UP:
            self.y -= self.bspeed
        if self.dir & self.Direction.DOWN:
            self.y += self.bspeed

        if self.dir & self.Direction.LEFT:
            self.x -= self.bspeed
        if self.dir & self.Direction.RIGHT:
            self.x += self.bspeed

    def reset(self):
        self.x = 400

    def revert_dir(self):
        self.dir = ~self.dir

    def check_border(self, x, y):
        if self.x <= 0 or self.x > x:
            self.dir ^= self.Direction.LEFT | self.Direction.RIGHT
        if self.y <= 0 or self.y > y:
            self.dir ^= self.Direction.UP | self.Direction.DOWN

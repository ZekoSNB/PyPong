from pypong.canvas_obj import CanvasObject


class Player(CanvasObject):
    def __init__(self, x, y, screen) -> None:
        super().__init__(x, y, 20, 150, screen)
        self.speed = 5

    def move(self, direction: CanvasObject.Direction, y_limit):
        if direction & self.Direction.UP:
            self.y -= self.speed
        if direction & self.Direction.DOWN:
            self.y += self.speed

        self.y = min(self.y, y_limit - self.height)
        self.y = max(self.y, 0)

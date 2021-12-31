import pygame

from pypong.player import Player
from pypong.canvas_obj import CanvasObject
# from pypong.ball import Ball


class Game(CanvasObject):
    # TODO: add ball
    def __init__(self) -> None:
        super().__init__()
        self.HEIGHT, self.WIDTH = 600, 900
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(50, 150, self.screen)
        self.p2 = Player(850, 150, self.screen)
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        
        self.running = True

    def run(self):
         
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_w:
                        self.up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.up = False
            self.p2.render()
            self.p1.render()
            self.p1.move()
            # self.p2.move()
            # print(self.up)
            pygame.display.update()

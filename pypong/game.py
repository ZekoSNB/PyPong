import pygame

from pypong.player import Player
from pypong.canvas_obj import CanvasObject
from pypong.ball import Ball


class Game(CanvasObject):
    # TODO: add ball
    def __init__(self) -> None:
        super().__init__()
        self.HEIGHT, self.WIDTH = 600, 900
        self.scrcolor = (0,0,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(50, 150, self.screen)
        self.p2 = Player(850, 150, self.screen)
        self.ball = Ball(450,300, self.screen)
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        
        self.running = True

    def run(self):
         
        while self.running:
            self.clock.tick(60)
            self.screen.fill(self.scrcolor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_w:
                        self.upp1 = True
                    if event.key == pygame.K_s:
                        self.downp1 = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.upp1 = False
                    if event.key == pygame.K_s:
                        self.downp1 = False
            self.p2.render()
            self.p1.render()
            self.ball.render()
            self.p1.move(self.upp1, self.downp1)
            # self.p2.move()
            pygame.display.update()

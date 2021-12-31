import pygame

from pypong.player import Player
# from pypong.ball import Ball


class Game:
    # TODO: add player2
    # TODO: add ball
    def __init__(self) -> None:
        self.HEIGHT, self.WIDTH = 600, 900
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(50, 150, self.screen)
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
            self.p1.render()
            pygame.display.update()

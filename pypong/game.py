import pygame

from pypong.player import Player
from pypong.ball import Ball


class Game:
    def __init__(self) -> None:
        self.pwidth, self.pheight = 20, 100
        self.HEIGHT, self.WIDTH = 600, 900
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(50, 150, 5, self.pwidth, self.pheight, self.screen)
        pygame.init()
        self.rectcolor = (255, 255, 255)
        pygame.display.set_caption('Pong ^-^')
        self.running = True

    def run(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.p1.render()
        print(self.screen, self.y)

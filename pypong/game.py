import pygame

from pypong.player import Player
from pypong.ball import Ball

Dir = Player.Direction


class Game:
    def __init__(self) -> None:
        self.width = 900
        self.height = 600
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        # self.scr_font = pygame.font.Font('assets/fonts/Gamer.ttf', 56)
        self.scrcolor = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.p1 = Player(50, 0, self.screen)
        self.p2 = Player(850, 150, self.screen)
        self.ball = Ball(300, 450, self.screen)
        self.pressed_keys = set()
        self.running = True

        self.count1 = 0
        self.count2 = 0

    def key_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.pressed_keys.add(event.key)
            if event.type == pygame.KEYUP:
                self.pressed_keys.discard(event.key)

    def event(self):
        for key in self.pressed_keys:
            if key == pygame.K_w:
                self.p1.move(Dir.UP, self.height)
            if key == pygame.K_s:
                self.p1.move(Dir.DOWN, self.height)
            if key == pygame.K_l:
                self.p2.move(Dir.DOWN, self.height)
            if key == pygame.K_o:
                self.p2.move(Dir.UP, self.height)

    def run(self):
        while self.running:
            # Game functions
            self.clock.tick(60)
            self.screen.fill(self.scrcolor)
            self.score(234, 0)

            self.event()
            self.key_event()

            # Player Functions
            self.p2.render()
            self.p1.render()
            # Ball Functions
            self.ball.move()
            self.ball.render()
            self.ball.check_border(self.width, self.height)
            # Collision
            if self.p1.collision(self.ball) or self.p2.collision(self.ball):
                self.ball.revert_dir()
            # Display Update
            pygame.display.flip()

    def score(self, x, y):
        return
        text = self.scr_font.render(f"Player1: {num1} | Player2: {num2}", True, (255, 255, 255))
        screen.blit(text, (x, y))

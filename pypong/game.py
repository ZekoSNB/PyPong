import pygame

from pypong.player import Player
from pypong.canvas_obj import CanvasObject
from pypong.ball import Ball


class Game(CanvasObject):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        self.scr_font = pygame.font.Font('assets/fonts/Gamer.ttf', 56)
        self.scrcolor = (0,0,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(self.px1, self.py1, self.screen)
        self.p2 = Player(self.px2, self.py2, self.screen)
        self.ball = Ball(self.x, self.y , self.screen)
        self.running = True
    def fevent(self):
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
                    if event.key == pygame.K_l:
                        self.downp2 = True
                    if event.key == pygame.K_o:
                        self.upp2 = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.upp1 = False
                    if event.key == pygame.K_s:
                        self.downp1 = False
                    if event.key == pygame.K_l:
                        self.downp2 = False
                    if event.key == pygame.K_o:
                        self.upp2 = False
    def event(self):
        if self.ball.border() == 'down':
            self.down = True
            self.up = False
        if self.ball.border() == 'up':
            self.up = True
            self.down = False
        if self.ball.x < 0:
            self.ball.reset()
            self.count1 += 1
            self.right = True
            self.left = False
        if self.ball.x > 900:
            self.ball.reset()
            self.count2 += 1
            self.right = False
            self.left = True
        if self.collision(self.p1.x, self.p1.y, self.ball.x, self.ball.y, self.p1):
            self.right = True
            self.left = False
        if self.collision(self.p2.x, self.p2.y, self.ball.x, self.ball.y, self.p2):
            self.right = False
            self.left = True
        if self.p1.y > 470:
            self.downp1 = False
        if self.p1.y < 0:
            self.upp1 = False
        if self.p2.y > 470:
            self.downp2 = False
        if self.p2.y < 0:
            self.upp2 = False
    def run(self):
        while self.running:
            # Game functions
            self.clock.tick(60)
            self.screen.fill(self.scrcolor)
            self.score(self.count1,self.count2, self.screen, 234,0)
            self.event()
            self.fevent()
            # Player Functions
            self.p1.move(self.upp1, self.downp1)
            self.p2.move(self.upp2, self.downp2)
            self.p2.render()
            self.p1.render()
            # Ball Functions
            self.ball.render()
            self.ball.move(self.up,self.down,self.left,self.right)
            self.ball.border()
            # Collision
            # self.collision(self.p1.x,self.p1.y,self.ball.x, self.ball.y)
            # Display Update 
            pygame.display.flip()

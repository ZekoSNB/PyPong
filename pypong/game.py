import pygame

from pypong.player import Player
from pypong.canvas_obj import CanvasObject
from pypong.ball import Ball


class Game(CanvasObject):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        self.scrcolor = (0,0,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(self.px1, self.py1, self.screen)
        self.p2 = Player(self.px2, self.py2, self.screen)
        self.ball = Ball(self.x, self.y , self.screen)
        self.myfont = pygame.font.SysFont('Monospace Regular', 30)
        self.textsurface = self.myfont.render('Score:(NONE)',False,(255,255,255))
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


    def run(self):
        while self.running:
            # Game functions
            self.screen.blit(self.textsurface,(450, 300))
            self.clock.tick(60)
            self.screen.fill(self.scrcolor)
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
            self.collision(self.p1.x,self.p1.y,self.ball.x, self.ball.y)
            # Display Update 
            pygame.display.update()

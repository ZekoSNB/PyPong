import pygame

from pypong.player import Player
from pypong.canvas_obj import CanvasObject
from pypong.ball import Ball


class Game(CanvasObject):
    # TODO: add ball
    def __init__(self) -> None:
        super().__init__()
        self.scrcolor = (0,0,0)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.p1 = Player(50, 150, self.screen)
        self.p2 = Player(850, 150, self.screen)
        self.ball = Ball(self.x, self.y , self.screen)
        
        pygame.init()
        pygame.display.set_caption('Pong ^-^')
        
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


    def run(self):
        while self.running:
            # Game functions
            self.clock.tick(60)
            self.screen.fill(self.scrcolor)
            self.fevent()
            # Player Functions
            self.p1.move(self.upp1, self.downp1)
            self.p2.move(self.upp2, self.downp2)
            self.p2.render()
            self.p1.render()
            # Ball Functions
            self.ball.render()
            self.ball.move(self.up,self.down,self.left,self.right)
            print(self.up,self.down,self.right,self.left)
            self.ball.border()
            # Display Update 
            pygame.display.update()

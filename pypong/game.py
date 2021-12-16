import pygame
from Player import playerobj

class game():
    def __init__(self) -> None:
        self.pwidth , self.pheight = 20,100
        self.p1 = playerobj(50,150,5,self.pwidth,self.pheight)
        self.HEIGHT, self.WIDTH = 600,900
        pygame.init()
        self.rectcolor = (255,255,255)
        pygame.display.set_caption('Pong ^-^')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
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
        



if __name__ == '__main__':
    grun = game()
    grun.run()
import pygame

from game.scenes.overworld import Overworld

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1024, 576))
        pygame.display.set_caption("Project Pokemon")

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.scene = Overworld(self)

        self.running = False
    
    def run(self):
        self.running = True

        self.scene.start()

        while self.running:
            self.scene.update(self.delta)

            self.delta = self.clock.tick(60)

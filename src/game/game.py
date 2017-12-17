import pygame

import game.data
from game.scene import Scene

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        self.window = pygame.display.set_mode((1024, 576))
        pygame.display.set_caption("Project Pokemon")

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.scene = Scene(self, 'battle')

        self.running = False
    
    def run(self):
        self.running = True

        self.scene.start()

        while self.running:
            self.scene.update(self.delta)

            self.delta = self.clock.tick(60)

    def set_scene(self, scene):
        scene.prev = self.scene
        self.scene = scene
        self.scene.start()
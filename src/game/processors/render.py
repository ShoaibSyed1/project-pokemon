import pygame

from esper import Processor

class RenderProcessor(Processor):
    def __init__(self, window):
        self.window = window
    
    def process(self):
        self.window.fill((255, 255, 255))

        pygame.display.flip()

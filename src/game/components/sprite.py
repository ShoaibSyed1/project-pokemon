import pygame

class Sprite:
    def __init__(self, surface, bounds=None, scale=1, layer=0):
        self.layer = layer
        self.surface = surface
        if bounds == None:
            bounds = surface.get_rect()
        
        bounds = pygame.Rect(bounds.left * scale, bounds.top * scale, bounds.width * 2, bounds.height * 2)
        self.bounds = bounds
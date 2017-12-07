import pygame

class Sprite:
    def __init__(self, surface, bounds=None, layer=0):
        self.layer = layer
        self.surface = surface
        if bounds == None:
            bounds = surface.get_rect()
        
        bounds = pygame.Rect(bounds.left, bounds.top, bounds.width, bounds.height)
        self.bounds = bounds
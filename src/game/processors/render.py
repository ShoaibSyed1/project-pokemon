import pygame

from esper import Processor

from game.components.sprite import Sprite
from game.components.transform import Transform
from game.math.vector2 import Vector2

class RenderProcessor(Processor):
    def __init__(self, window):
        self.window = window
    
    def process(self, delta):
        self.window.fill((255, 255, 255))
        
        for ent, (spr, transform) in self.world.get_components(Sprite, Transform):
            temp_surface = spr.surface
            if transform.scale != Vector2(1.0, 1.0):
                temp_surface = pygame.transform.scale(
                    temp_surface,
                    (int(transform.scale.x * spr.surface.get_width()),
                     int(transform.scale.y * spr.surface.get_height())))
            self.window.blit(temp_surface, (transform.pos.x, transform.pos.y))

        pygame.display.flip()

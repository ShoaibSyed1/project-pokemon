import pygame

from esper import Processor

from pygame.math import Vector2

from game.components import Sprite, Transform

class RenderProcessor(Processor):
    def __init__(self, window, camera_entity):
        self.window = window
        self.camera_entity = camera_entity
        self.batch = pygame.surface.Surface((640, 480))
    
    def process(self, delta):
        self.window.fill((255, 255, 255))
        self.batch.fill((255, 255, 255))

        camera_pos = self.world.component_for_entity(self.camera_entity, Transform)

        draws = []
        
        for ent, (spr, transform) in self.world.get_components(Sprite, Transform):
            temp_surface = spr.surface
            if transform.scale != Vector2(1.0, 1.0):
                temp_surface = pygame.transform.scale(
                    temp_surface,
                    (int(transform.scale.x * spr.surface.get_width()),
                     int(transform.scale.y * spr.surface.get_height())))
            
            draws.append((temp_surface, (transform.pos.x - camera_pos.pos.x,
                                            transform.pos.y - camera_pos.pos.y), spr.bounds, spr.layer))
        
        draws.sort(key=lambda x: x[3])

        for d in draws:
            self.batch.blit(d[0], d[1], d[2])
        
        self.window.blit(self.batch, (0, 0))

        pygame.display.flip()

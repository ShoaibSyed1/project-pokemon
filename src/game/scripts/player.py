from enum import Enum

import pygame

from game.components import InputComponent
from game.components.tile import Direction, Tile
from game.components.transform import Transform
from game.scripts.script import Script

class PlayerScript(Script):    
    def start(self):
        self.input = self.world.component_for_entity(self.entity, InputComponent)
        self.tile = self.world.component_for_entity(self.entity, Tile)
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        print(self.tile.is_moving)
        if not self.tile.is_moving:
            if self.input.keys[pygame.K_w]:
                self.tile.move_path.insert(0, Direction.UP)
            elif self.input.keys[pygame.K_s]:
                self.tile.move_path.insert(0, Direction.DOWN)
            elif self.input.keys[pygame.K_a]:
                self.tile.move_path.insert(0, Direction.LEFT)
            elif self.input.keys[pygame.K_d]:
                self.tile.move_path.insert(0, Direction.RIGHT)
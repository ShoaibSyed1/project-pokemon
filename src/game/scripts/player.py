from enum import Enum

import pygame

from game.components import AnimationGroups, InputComponent
from game.components.tile import Direction, Tile
from game.components.transform import Transform
from game.scripts.script import Script

class PlayerScript(Script):
    def start(self):
        self.anim_groups = self.world.component_for_entity(self.entity, AnimationGroups)
        self.input = self.world.component_for_entity(self.entity, InputComponent)
        self.tile = self.world.component_for_entity(self.entity, Tile)
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        if not self.tile.is_moving:
            self.anim_groups.current = 'still'
            if self.input.keys[pygame.K_w]:
                self.tile.move_path.insert(0, Direction.UP)
            elif self.input.keys[pygame.K_s]:
                self.tile.move_path.insert(0, Direction.DOWN)
            elif self.input.keys[pygame.K_a]:
                self.tile.move_path.insert(0, Direction.LEFT)
            elif self.input.keys[pygame.K_d]:
                self.tile.move_path.insert(0, Direction.RIGHT)
        else:
            if self.tile.move_dir == Direction.DOWN:
                self.anim_groups.current = 'walk_down'